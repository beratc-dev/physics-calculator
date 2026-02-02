from core.quantities import Quantity
from core.solver import Solver


def Q(key, value=None, unit=None, domain="mechanics", is_delta=False):
    return Quantity(
        key=key,
        name=key,
        symbol=key,
        value=value,
        unit=unit,
        domain=domain,
        is_delta=is_delta
    )

def test_solver_simple_speed():
    solver = Solver()

    d = Q("distance", 20, "m", is_delta=True)
    t = Q("time", 4, "s", is_delta=True)

    solver.add(d)
    solver.add(t)

    v = solver.solve("velocity")

    assert isinstance(v, Quantity)
    assert v.key == "speed"
    assert v.value == 5
    assert v.unit == "m/s"
    assert v.is_delta is False
    assert v.domain == "mechanics"   

def test_speed_negative_time_raises_error():
    solver = Solver()

    d = Q("distance", 10, "m", is_delta=True)
    t = Q("time", -2, "s", is_delta=True)

    solver.add(d)
    solver.add(t)

    try:
        solver.solve("speed")
        assert False
    except ValueError:
        assert True
