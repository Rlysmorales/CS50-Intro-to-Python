from twttr_used_testing import shorten


def test_shorten():
    assert shorten("arelys") == 'rlys'


def test_cap_vowel():
    assert shorten("ARelys") == 'Rlys'


def test_number_vowel():
    assert shorten("arelys123") == 'rlys123'


def test_pun_vowel():
    assert shorten("arelys12.") == 'rlys12.'



def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
