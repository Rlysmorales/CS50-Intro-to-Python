from bank import value


def test_value_hello():
    assert value("hello") == 0


def test_value_h():
    assert value("hope") == 20


def test_value_capital():
    assert value("HOPE") == 20


def test_value_no_h():
    assert value("Wepa") == 100
