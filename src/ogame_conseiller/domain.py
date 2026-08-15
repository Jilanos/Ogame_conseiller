from __future__ import annotations

from dataclasses import dataclass, field, replace
from math import ceil
from typing import Literal

Resource = Literal["metal", "crystal", "deuterium"]
RESOURCES: tuple[Resource, ...] = ("metal", "crystal", "deuterium")


@dataclass(frozen=True)
class Rules:
    """Paramètres versionnés ; ils évitent de coder les hypothèses d'univers."""

    economy_speed: float = 1.0
    metal_base: float = 30.0
    crystal_base: float = 20.0
    deuterium_base: float = 10.0
    production_exponent: float = 1.1
    deuterium_exponent: float = 1.5
    solar_base: float = 20.0
    construction_factor: float = 2500.0
    metal_cost_base: float = 60.0
    crystal_cost_base: float = 15.0
    deuterium_cost_base: float = 0.0
    cost_multiplier: float = 1.5

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
        return base * level * self.production_exponent**exponent * self.economy_speed

    def energy_production(self, level: int) -> float:
        return self.solar_base * level * self.production_exponent**level

    def cost(self, kind: Resource, next_level: int) -> dict[Resource, float]:
        if next_level < 1:
            raise ValueError("next_level doit être positif")
        multiplier = self.cost_multiplier ** (next_level - 1)
        base = {
            "metal": self.metal_cost_base,
            "crystal": self.crystal_cost_base,
            "deuterium": self.deuterium_cost_base,
        }[kind]
        # Mine de métal/cristal/deut : coûts différenciés par ressource.
        if kind == "metal":
            return {"metal": 60 * multiplier, "crystal": 15 * multiplier, "deuterium": 0}
        if kind == "crystal":
            return {"metal": 48 * multiplier, "crystal": 24 * multiplier, "deuterium": 0}
        return {"metal": 225 * multiplier, "crystal": 75 * multiplier, "deuterium": 0}

    def construction_hours(self, costs: dict[Resource, float]) -> float:
        total = costs["metal"] + costs["crystal"]
        return max(0.01, total / (self.construction_factor * self.economy_speed))


@dataclass(frozen=True)
class Planet:
    name: str
    metal_mine: int = 1
    crystal_mine: int = 1
    deuterium_synthesizer: int = 1
    solar_plant: int = 1
    metal: float = 0.0
    crystal: float = 0.0
    deuterium: float = 0.0
    available_at: float = 0.0
    cumulative: dict[Resource, float] = field(default_factory=lambda: {r: 0.0 for r in RESOURCES})

    def level(self, kind: Resource) -> int:
        return {"metal": self.metal_mine, "crystal": self.crystal_mine, "deuterium": self.deuterium_synthesizer}[kind]

    def production(self, rules: Rules) -> dict[Resource, float]:
        return {r: rules.production_per_hour(r, self.level(r)) for r in RESOURCES}

    def energy_balance(self, rules: Rules) -> float:
        consumption = self.metal_mine * 10 + self.crystal_mine * 10 + self.deuterium_synthesizer * 20
        return rules.energy_production(self.solar_plant) - consumption


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
        amounts = {r: getattr(planet, r) + prod[r] * hours for r in RESOURCES}
        cumulative = {r: planet.cumulative[r] + prod[r] * hours for r in RESOURCES}
        return replace(planet, **amounts, cumulative=cumulative)

    def buy(self, planet: Planet, kind: Resource, start: float) -> tuple[Planet, float, dict[Resource, float]] | None:
        level = planet.level(kind)
        costs = self.rules.cost(kind, level + 1)
        available = max(start, planet.available_at)
        # La planète peut être restée inactive pendant que l'empire construisait
        # ailleurs : il faut alors accumuler sa production depuis son propre
        # dernier événement, pas depuis l'horloge globale de l'action.
        advanced = self.advance_planet(planet, available - planet.available_at)
        if any(getattr(advanced, r) + 1e-9 < costs[r] for r in RESOURCES):
            return None
        after_payment = {r: getattr(advanced, r) - costs[r] for r in RESOURCES}
        duration = self.rules.construction_hours(costs)
        finished = available + duration
        completed = self.advance_planet(replace(advanced, **after_payment), duration)
        levels = {"metal": "metal_mine", "crystal": "crystal_mine", "deuterium": "deuterium_synthesizer"}
        completed = replace(completed, **{levels[kind]: level + 1}, available_at=finished)
        return completed, finished, costs
