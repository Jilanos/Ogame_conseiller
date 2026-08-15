from __future__ import annotations

from dataclasses import dataclass, field, replace
from math import floor
from typing import Literal

Resource = Literal["metal", "crystal", "deuterium"]
Buildable = Literal["metal", "crystal", "deuterium", "solar", "metal_storage", "crystal_storage", "deuterium_tank"]
RESOURCES: tuple[Resource, ...] = ("metal", "crystal", "deuterium")


@dataclass(frozen=True)
class Rules:
    """Paramètres versionnés ; ils évitent de coder les hypothèses d'univers."""

    economy_speed: float = 1.0
    metal_base: float = 30.0
    crystal_base: float = 20.0
    deuterium_base: float = 10.0
    base_metal_production: float = 30.0
    base_crystal_production: float = 15.0
    production_exponent: float = 1.1
    deuterium_exponent: float = 1.0
    solar_base: float = 20.0
    construction_factor: float = 2500.0
    metal_cost_base: float = 60.0
    crystal_cost_base: float = 15.0
    deuterium_cost_base: float = 0.0
    cost_multiplier: float = 1.5
    crystal_cost_multiplier: float = 1.6
    storage_capacity_base: float = 10_000.0
    storage_capacity_multiplier: float = 2.0
    offline_hours: float = 8.0

    def production_per_hour(self, resource: Resource, level: int) -> float:
        if level <= 0:
            return 0.0
        if resource == "metal":
            base = self.metal_base
            exponent = level
        elif resource == "crystal":
            base = self.crystal_base
            exponent = level
        else:
            base = self.deuterium_base
            exponent = self.deuterium_exponent * level
        mine_production = base * level * self.production_exponent**exponent * self.economy_speed
        base_production = {
            "metal": self.base_metal_production,
            "crystal": self.base_crystal_production,
            "deuterium": 0.0,
        }[resource] * self.economy_speed
        return mine_production + base_production

    def energy_production(self, level: int) -> float:
        return self.solar_base * level * self.production_exponent**level

    def cost(self, kind: Buildable, next_level: int) -> dict[Resource, float]:
        if next_level < 1:
            raise ValueError("next_level doit être positif")
        multiplier = self.cost_multiplier ** (next_level - 1)
        if kind == "metal":
            return {"metal": 60 * multiplier, "crystal": 15 * multiplier, "deuterium": 0}
        if kind == "crystal":
            crystal_multiplier = self.crystal_cost_multiplier ** (next_level - 1)
            return {"metal": 48 * crystal_multiplier, "crystal": 24 * crystal_multiplier, "deuterium": 0}
        if kind == "deuterium":
            return {"metal": 225 * multiplier, "crystal": 75 * multiplier, "deuterium": 0}
        if kind == "solar":
            return {"metal": 75 * multiplier, "crystal": 30 * multiplier, "deuterium": 0}
        storage_multiplier = self.storage_capacity_multiplier ** (next_level - 1)
        if kind == "metal_storage":
            return {"metal": 1_000 * storage_multiplier, "crystal": 0, "deuterium": 0}
        if kind == "crystal_storage":
            return {"metal": 1_000 * storage_multiplier, "crystal": 500 * storage_multiplier, "deuterium": 0}
        return {"metal": 1_000 * storage_multiplier, "crystal": 1_000 * storage_multiplier, "deuterium": 0}

    def construction_hours(self, costs: dict[Resource, float]) -> float:
        total = costs["metal"] + costs["crystal"]
        return max(0.01, total / (self.construction_factor * self.economy_speed))

    def next_online_hour(self, hour: float) -> float:
        """Suppose que l'heure zéro est la connexion du matin, suivie de 8 h off."""
        active_hours = 24.0 - self.offline_hours
        day_start = floor(hour / 24.0) * 24.0
        if hour - day_start <= active_hours:
            return hour
        return day_start + 24.0


@dataclass(frozen=True)
class Planet:
    name: str
    metal_mine: int = 1
    crystal_mine: int = 1
    deuterium_synthesizer: int = 1
    solar_plant: int = 1
    metal_storage: int = 0
    crystal_storage: int = 0
    deuterium_tank: int = 0
    metal: float = 0.0
    crystal: float = 0.0
    deuterium: float = 0.0
    available_at: float = 0.0
    cumulative: dict[Resource, float] = field(default_factory=lambda: {r: 0.0 for r in RESOURCES})

    def level(self, kind: Resource) -> int:
        return {"metal": self.metal_mine, "crystal": self.crystal_mine, "deuterium": self.deuterium_synthesizer}[kind]

    def level_of(self, kind: Buildable) -> int:
        return {
            "metal": self.metal_mine,
            "crystal": self.crystal_mine,
            "deuterium": self.deuterium_synthesizer,
            "solar": self.solar_plant,
            "metal_storage": self.metal_storage,
            "crystal_storage": self.crystal_storage,
            "deuterium_tank": self.deuterium_tank,
        }[kind]

    def production(self, rules: Rules) -> dict[Resource, float]:
        return {r: rules.production_per_hour(r, self.level(r)) for r in RESOURCES}

    def energy_balance(self, rules: Rules) -> float:
        consumption = (
            10 * self.metal_mine * rules.production_exponent**self.metal_mine
            + 10 * self.crystal_mine * rules.production_exponent**self.crystal_mine
            + 20 * self.deuterium_synthesizer * rules.production_exponent**self.deuterium_synthesizer
        )
        return rules.energy_production(self.solar_plant) - consumption

    def capacity(self, resource: Resource, rules: Rules) -> float:
        level = {
            "metal": self.metal_storage,
            "crystal": self.crystal_storage,
            "deuterium": self.deuterium_tank,
        }[resource]
        return rules.storage_capacity_base * rules.storage_capacity_multiplier**level


@dataclass(frozen=True)
class Empire:
    planets: tuple[Planet, ...]
    rules: Rules = field(default_factory=Rules)
    weights: dict[Resource, float] = field(default_factory=lambda: {"metal": 1.0, "crystal": 1.0, "deuterium": 1.0})

    @classmethod
    def from_dict(cls, raw: dict) -> "Empire":
        rules = Rules(**raw.get("rules", {}))
        planets = tuple(Planet(**item) for item in raw.get("planets", []))
        if not planets:
            raise ValueError("L'empire doit contenir au moins une planète")
        weights = {**{"metal": 1.0, "crystal": 1.0, "deuterium": 1.0}, **raw.get("weights", {})}
        return cls(planets=planets, rules=rules, weights=weights)

    def total_production(self) -> dict[Resource, float]:
        return {r: sum(p.production(self.rules)[r] for p in self.planets) for r in RESOURCES}

    def weighted(self, amounts: dict[Resource, float]) -> float:
        return sum(amounts[r] * self.weights.get(r, 1.0) for r in RESOURCES)

    def advance_planet(self, planet: Planet, hours: float) -> Planet:
        if hours <= 0:
            return planet
        prod = planet.production(self.rules)
        amounts = {r: min(planet.capacity(r, self.rules), getattr(planet, r) + prod[r] * hours) for r in RESOURCES}
        # Une ressource qui heurte son entrepôt ne compte pas dans la production
        # effectivement récupérable : le planificateur doit donc financer les
        # entrepôts ou une dépense avant une période hors-ligne.
        cumulative = {r: planet.cumulative[r] + amounts[r] - getattr(planet, r) for r in RESOURCES}
        return replace(planet, **amounts, cumulative=cumulative)

    def buy(self, planet: Planet, kind: Buildable, start: float) -> tuple[Planet, float, dict[Resource, float]] | None:
        level = planet.level_of(kind)
        costs = self.rules.cost(kind, level + 1)
        storage_for_cost = {
            "metal": planet.capacity("metal", self.rules),
            "crystal": planet.capacity("crystal", self.rules),
            "deuterium": planet.capacity("deuterium", self.rules),
        }
        # Une construction ne peut pas être financée par une ressource que la
        # capacité actuelle ne pourra jamais contenir.
        if any(costs[r] > storage_for_cost[r] + 1e-9 for r in RESOURCES):
            return None
        available = self.rules.next_online_hour(max(start, planet.available_at))
        # La planète peut être restée inactive pendant que l'empire construisait
        # ailleurs : il faut alors accumuler sa production depuis son propre
        # dernier événement, pas depuis l'horloge globale de l'action.
        advanced = self.advance_planet(planet, available - planet.available_at)
        deficits = {r: max(0.0, costs[r] - getattr(advanced, r)) for r in RESOURCES}
        if any(deficits.values()):
            production = advanced.production(self.rules)
            waits = []
            for resource, deficit in deficits.items():
                if deficit <= 0:
                    continue
                if production[resource] <= 0:
                    return None
                waits.append(deficit / production[resource])
            wait = max(waits, default=0.0)
            advanced = self.advance_planet(advanced, wait)
            ready_at = available + wait
            available = self.rules.next_online_hour(ready_at)
            advanced = self.advance_planet(advanced, available - ready_at)
        after_payment = {r: getattr(advanced, r) - costs[r] for r in RESOURCES}
        duration = self.rules.construction_hours(costs)
        finished = available + duration
        completed = self.advance_planet(replace(advanced, **after_payment), duration)
        levels = {
            "metal": "metal_mine", "crystal": "crystal_mine", "deuterium": "deuterium_synthesizer", "solar": "solar_plant",
            "metal_storage": "metal_storage", "crystal_storage": "crystal_storage", "deuterium_tank": "deuterium_tank",
        }
        completed = replace(completed, **{levels[kind]: level + 1}, available_at=finished)
        return completed, finished, costs
