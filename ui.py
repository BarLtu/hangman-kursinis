class ConsoleUI:
    HANGMAN_STAGES = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |      
           -
        """
    ]

    def display_game_state(self, status):
        print("\n" * 2)
        print(self.HANGMAN_STAGES[status['attempts_left']])
        print(f"Word: {status['display_word']}")
        print(f"Attempts left: {status['attempts_left']}")
        print(f"Wrong guesses: {', '.join(status['wrong_guesses'])}")
        print(f"Player score: {status['score']}")
        print("-" * 20)

    def get_user_input(self):
        while True:
            guess = input("Guess a letter: ").strip().upper()
            if len(guess) == 1 and guess.isalpha():
                return guess
            print("Error! Enter a single letter.")

    def show_message(self, message):
        print(f"\n>>> {message} <<<")