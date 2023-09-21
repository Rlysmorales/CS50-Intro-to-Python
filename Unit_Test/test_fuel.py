from fuel import convert, gauge
import pytest


def test_convert_percent():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('4/4') == 100


def test_gauge_percent():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_division_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert('4/0')


def test_value_error():
    with pytest.raises(ValueError):
        convert('cat/dog')
