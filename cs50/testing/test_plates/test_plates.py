import plates
import pytest


def test_isvalid():
    assert plates.is_valid("CS50")
    assert plates.is_valid("CS50")
    assert not plates.is_valid("CS50P")
    assert not plates.is_valid("CS50PS")
    assert not plates.is_valid("C")
    assert not plates.is_valid("CS50PS1")
    assert not plates.is_valid("CS5P0")
    assert not plates.is_valid("CS05")
    assert not plates.is_valid("CS 50")
    assert not plates.is_valid("CS-50")
    assert not plates.is_valid("CS50P1")
    assert not plates.is_valid("5HELLO")
    assert not plates.is_valid("A50")

