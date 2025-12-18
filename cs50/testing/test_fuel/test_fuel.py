import fuel
import pytest

def test_convert():
    assert fuel.convert("1/5") == 20
    assert not fuel.convert("1/3") == 34
    with pytest.raises(ValueError):
        fuel.convert("3/2")
    with pytest.raises(ValueError):
        fuel.convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_gauge():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(60) == "60%"


