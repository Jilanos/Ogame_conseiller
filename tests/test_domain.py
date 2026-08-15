from ogame_conseiller.domain import Empire, Planet, Rules


def test_production_is_positive_and_increases_with_level():
    rules = Rules()
    assert rules.production_per_hour("metal", 1) > 0
    assert rules.production_per_hour("metal", 5) > rules.production_per_hour("metal", 4)


def test_observed_mine_production_includes_universe_speed_and_base_income():
    rules = Rules(economy_speed=8)
    assert round(rules.production_per_hour("metal", 15)) == 15_278
    assert round(rules.production_per_hour("crystal", 11)) == 5_141


def test_empire_rejects_empty_planets():
    try:
        Empire.from_dict({"planets": []})
    except ValueError as exc:
        assert "au moins une" in str(exc)
    else:
        raise AssertionError("empty empire should fail")


def test_planet_energy_balance_is_explicit():
    planet = Planet("A", metal_mine=10, crystal_mine=10, deuterium_synthesizer=10, solar_plant=1)
    assert planet.energy_balance(Rules()) < 0


def test_observed_energy_formula_matches_the_ogame_screen_values():
    planet = Planet("A", metal_mine=15, crystal_mine=11, deuterium_synthesizer=5, solar_plant=14)
    assert round(planet.energy_balance(Rules())) in {-37, -38}


def test_resources_stop_at_storage_capacity():
    planet = Planet("A", metal_storage=1)
    advanced = Empire((planet,)).advance_planet(planet, 10_000)
    assert advanced.metal == 20_000


def test_mine_cannot_be_bought_when_cost_exceeds_storage_capacity():
    empire = Empire((Planet("A", metal_mine=19, crystal_mine=11, metal_storage=3, crystal_storage=3),))
    assert empire.buy(empire.planets[0], "metal", 0) is None


def test_next_online_hour_defers_actions_during_night():
    rules = Rules(offline_hours=8)
    assert rules.next_online_hour(15.9) == 15.9
    assert rules.next_online_hour(16.1) == 24.0
