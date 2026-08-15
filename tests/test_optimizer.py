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


def test_optimizer_waits_for_resources_when_starting_from_zero():
    result = optimize(Empire.from_dict({"planets": [{"name": "Alpha", "metal_mine": 4, "crystal_mine": 3, "deuterium_synthesizer": 1, "solar_plant": 8}]}), 10, max_actions=1)
    assert result.actions
    assert result.actions[0].start_hour > 0


def test_energy_deficit_prioritizes_solar_plant():
    empire_with_deficit = Empire.from_dict({"planets": [{"name": "Alpha", "metal_mine": 15, "crystal_mine": 11, "deuterium_synthesizer": 5, "solar_plant": 14, "metal_storage": 3, "crystal_storage": 3}]})
    result = optimize(empire_with_deficit, 10, max_actions=1)
    assert result.actions[0].kind == "solar"


def test_offline_window_prioritizes_required_storage():
    empire_with_small_storage = Empire.from_dict({"rules": {"economy_speed": 8}, "planets": [{"name": "Alpha", "metal_mine": 15, "crystal_mine": 11, "deuterium_synthesizer": 5, "solar_plant": 15, "metal_storage": 3, "crystal_storage": 3, "deuterium_tank": 1}]})
    result = optimize(empire_with_small_storage, 10, max_actions=1)
    assert result.actions[0].kind == "metal_storage"
