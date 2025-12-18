import pytest
from convert import convert

def test_int_conversion():
    assert convert(1) == 149597870700
    assert convert(2) == 299195741400

def test_zero():
    assert convert(0) == 0

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2) # 1e-2 same as .001

def test_error():
    with pytest.raises(TypeError):
        convert("cat")
    with pytest.raises(TypeError):
        convert("1")


