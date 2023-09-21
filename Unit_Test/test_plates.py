from plates import is_valid


def main():
    test_validate_true()
    test_validate_false()


def test_validate_true():
    assert is_valid("CS50") is True
    assert is_valid("CS") is True


def test_validate_false():
    assert is_valid("CS05") is False
    assert is_valid("CS50P") is False
    assert is_valid("PI3.14") is False
    assert is_valid("OUTATIME") is False
    assert is_valid("O") is False
    assert is_valid("123Are") is False
    assert is_valid("12") is False


if __name__ == "__main__":
    main()
