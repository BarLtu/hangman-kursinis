from models import GameWord


class HangmanEngine:
    def __init__(self, player, word_source):
        self.player = player
        self.word_source = word_source
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        self.game_word = None
        self.is_running = False
        self.wrong_guesses = []

    def start_new_round(self):
        raw_word = self.word_source.get_word()
        self.game_word = GameWord(raw_word)
        self.attempts_left = self.max_attempts
        self.wrong_guesses = []
        self.is_running = True

    def make_move(self, letter):
        if not self.is_running:
            return "Game is not running"

        letter = letter.upper()
        if letter in self.game_word.guessed_letters or letter in self.wrong_guesses:
            return "Already guessed"
        correct = self.game_word.check_letter(letter)

        if correct:
            if self.game_word.is_fully_guessed():
                self.is_running = False
                self.player.add_points(10)
                return "Correct! You've guessed the word!"
            return "Correct!"
        else:
            self.wrong_guesses.append(letter)
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.is_running = False
                return f"Game Over! The word was: {self.game_word.word}"
            return "Wrong!"

    def get_status(self):
        display_word = self.game_word.get_display_word()
        if not self.is_running and self.attempts_left == 0:
            display_word = self.game_word.word
        return {
            "display_word": display_word,
            "attempts_left": self.attempts_left,
            "wrong_guesses": self.wrong_guesses,
            "score": self.player.get_score()
        }