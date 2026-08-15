from ogame_conseiller.domain import Empire, Planet, Rules


def test_production_is_positive_and_increases_with_level():
    rules = Rules()
    assert rules.production_per_hour("metal", 1) > 0
    assert rules.production_per_hour("metal", 5) > rules.production_per_hour("metal", 4)


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
