import unittest
from unittest.mock import patch

from final_project import Hangman


class Test(unittest.TestCase):

    def test_yes_user_choice(self):
        with patch('builtins.input', return_value='yes') as mock_input:
            Hangman().user_choice()

            mock_input.assert_called_once()

    def test_no_user_choice(self):
        with patch('builtins.input', return_value='no') as mock_input:
            Hangman().user_choice()
            mock_input.assert_called_once()

    def test_outcome(self):
        assert display_game_outcome("You Win", "mike") == "You Win"
        assert display_game_outcome("You Lose", "mike") == "You Lose"

