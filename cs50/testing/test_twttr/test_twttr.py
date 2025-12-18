from twttr import shorten
import pytest

def test_shorten():
    assert shorten("hi") == "h"
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("Hello") == "Hll"

def test_numbers():
    assert shorten("h3ll0") == "h3ll0"
def test_punctuation():
    assert shorten("hello!") == "hll!"
def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
def test_empty_string():
    assert shorten("") == ""
