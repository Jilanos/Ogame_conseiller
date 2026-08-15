from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Iterable

from .domain import Empire, Planet, Resource, RESOURCES


@dataclass(frozen=True)
class Action:
    planet: str
    kind: Resource
    from_level: int
    to_level: int
    start_hour: float
    finish_hour: float
    costs: dict[Resource, float]


@dataclass(frozen=True)
class HorizonResult:
    days: int
    production: dict[Resource, float]
    baseline_production: dict[Resource, float]
    actions: tuple[Action, ...]
    score: float

    @property
    def uplift(self) -> dict[Resource, float]:
        return {r: self.production[r] - self.baseline_production[r] for r in RESOURCES}


@dataclass(frozen=True)
class _Candidate:
    empire: Empire
    actions: tuple[Action, ...]
    score: float


def _advance_all(empire: Empire, hours: float) -> Empire:
    return replace(empire, planets=tuple(empire.advance_planet(p, hours) for p in empire.planets))


def _to_horizon(empire: Empire, horizon: float) -> Empire:
    """Complète chaque planète depuis son propre dernier événement jusqu'à l'horizon."""
    return replace(
        empire,
        planets=tuple(empire.advance_planet(p, max(0.0, horizon - p.available_at)) for p in empire.planets),
    )


def _candidate_actions(empire: Empire, horizon_hours: float) -> Iterable[tuple[int, Resource]]:
    for index, planet in enumerate(empire.planets):
        if planet.available_at > horizon_hours:
            continue
        for kind in RESOURCES:
            # Les mines sont le cœur du MVP ; on n'ajoute une centrale que si l'énergie est déficitaire.
            if kind != "metal" and kind != "crystal" and planet.energy_balance(empire.rules) < 0:
                continue
            yield index, kind


def optimize(empire: Empire, days: int, *, beam_width: int = 12, max_actions: int = 14) -> HorizonResult:
    if days <= 0:
        raise ValueError("L'horizon doit être positif")
    horizon = days * 24.0
    baseline_empire = _to_horizon(empire, horizon)
    baseline = {r: sum(p.cumulative[r] for p in baseline_empire.planets) for r in RESOURCES}
    frontier = [_Candidate(empire, (), 0.0)]
    completed: list[_Candidate] = []
    for _ in range(max_actions):
        next_frontier: list[_Candidate] = []
        for candidate in frontier:
            frontier_time = max((p.available_at for p in candidate.empire.planets), default=0.0)
            for index, kind in _candidate_actions(candidate.empire, horizon):
                planet = candidate.empire.planets[index]
                result = candidate.empire.buy(planet, kind, frontier_time)
                if result is None:
                    continue
                updated_planet, finish, costs = result
                if finish > horizon:
                    continue
                planets = list(candidate.empire.planets)
                planets[index] = updated_planet
                updated = replace(candidate.empire, planets=tuple(planets))
                action = Action(planet.name, kind, planet.level(kind), planet.level(kind) + 1, max(frontier_time, planet.available_at), finish, costs)
                horizon_state = _to_horizon(updated, horizon)
                production = {r: sum(p.cumulative[r] for p in horizon_state.planets) for r in RESOURCES}
                score = updated.weighted(production)
                next_frontier.append(_Candidate(updated, candidate.actions + (action,), score))
        if not next_frontier:
            break
        next_frontier.sort(key=lambda c: (c.score, -len(c.actions)), reverse=True)
        frontier = next_frontier[:beam_width]
        completed.extend(frontier)
    best = max(completed or [_Candidate(empire, (), empire.weighted(baseline))], key=lambda c: c.score)
    final_state = _to_horizon(best.empire, horizon)
    production = {r: sum(p.cumulative[r] for p in final_state.planets) for r in RESOURCES}
    return HorizonResult(days, production, baseline, best.actions, empire.weighted(production))
