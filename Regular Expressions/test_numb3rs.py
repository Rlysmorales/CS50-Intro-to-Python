from numb3rs import validate


def test_validate():
    assert validate("255.255.255.255") is True
    assert validate("cat") is False
    assert validate("127.0.0.1") is True


def test_range():
    assert validate(r"25.2.3.1000") is False
    assert validate(r"256.256.256.256") is False
    assert validate(r"256.20.10.20") is False

