import pytest

from seasons import user_birthday_minutes, words_creation

def test_birth_minutes():
    assert user_birthday_minutes("1988-11-11") == 18341280


def test_words():
    assert words_creation(18341280) == "Eighteen million, three hundred forty-one thousand, two hundred eighty minutes"

