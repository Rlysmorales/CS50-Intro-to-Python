import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1


def test_deposit_value_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw_value_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(20)
