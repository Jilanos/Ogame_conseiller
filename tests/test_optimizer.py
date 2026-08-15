from ogame_conseiller.domain import Empire
from ogame_conseiller.optimizer import optimize


def empire():
    return Empire.from_dict({
        "planets": [
            {"name": "Alpha", "metal_mine": 8, "crystal_mine": 6, "deuterium_synthesizer": 4, "solar_plant": 12,
             "metal": 1000, "crystal": 1000, "deuterium": 500},
            {"name": "Beta", "metal_mine": 5, "crystal_mine": 4, "deuterium_synthesizer": 2, "solar_plant": 8,
             "metal": 1000, "crystal": 1000, "deuterium": 500},
        ]
    })


def test_optimizer_returns_three_horizon_shapes():
    result = optimize(empire(), 10, beam_width=4, max_actions=4)
    assert result.days == 10
    assert set(result.production) == {"metal", "crystal", "deuterium"}
    assert result.production["metal"] >= result.baseline_production["metal"]


def test_optimizer_is_deterministic():
    first = optimize(empire(), 30, beam_width=4, max_actions=5)
    second = optimize(empire(), 30, beam_width=4, max_actions=5)
    assert first == second


def test_upgrading_one_planet_does_not_lose_idle_planet_production():
    result = optimize(empire(), 10, beam_width=4, max_actions=4)
    assert result.production["deuterium"] >= result.baseline_production["deuterium"]
