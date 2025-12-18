from bank import value
import pytest

def test_int():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("bonjour") == 100

def test_case():
    assert value("HELLO") == 0
    assert value("BonJour") == 100
