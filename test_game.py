import unittest
from models import GameWord, Player
from engine import HangmanEngine


class TestHangmanGame(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestUser")
        class MockSource:
            def get_word(self):
                return "PYTHON"
        self.engine = HangmanEngine(self.player, MockSource())
        self.engine.start_new_round()

    def test_correct_guess(self):
        result = self.engine.make_move("P")
        self.assertEqual(result, "Correct!")
        self.assertIn("P", self.engine.game_word.guessed_letters)

    def test_wrong_guess(self):
        initial_attempts = self.engine.attempts_left
        result = self.engine.make_move("Z")
        self.assertEqual(result, "Wrong!")
        self.assertEqual(self.engine.attempts_left, initial_attempts - 1)

    def test_win_condition(self):
        self.engine.game_word = GameWord("A")
        result = self.engine.make_move("A")
        self.assertIn("Correct! You've guessed the word!", result)
        self.assertFalse(self.engine.is_running)

if __name__ == '__main__':
    unittest.main()