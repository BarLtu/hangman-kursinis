import sys
from models import Player
from factory import WordSourceFactory
from engine import HangmanEngine
from ui import ConsoleUI
from data_handler import DataHandler

def main():
    ui = ConsoleUI()
    db = DataHandler()
    factory = WordSourceFactory()

    print("=== Welcome to the Hangman Game ===")
    name = input("Enter your name: ").strip()
    if not name:
        name = "Anonymous"
    player = Player(name)

    print("\nChoose a word source:")
    print("1. Classic list (code)")
    print("2. Words from file (words.txt)")
    choice = input("Your choice (1/2): ")
    source_type = 'file' if choice == '2' else 'list'
    try:
        source = factory.get_word_source(source_type)
    except Exception as e:
        print(f"Error setting source: {e}. Using list.")
        source = factory.get_word_source('list')

    engine = HangmanEngine(player, source)

    while True:
        engine.start_new_round()
        ui.show_message(f"Good luck, {player.name}! The game begins.")

        while engine.is_running:
            status = engine.get_status()
            ui.display_game_state(status)
            guess = ui.get_user_input()
            result = engine.make_move(guess)
            ui.show_message(result)

        final_status = engine.get_status()
        ui.display_game_state(final_status)
        db.save_score(player.name, player.get_score())
        print("\n=== TOP 5 RESULTS ===")
        top_scores = db.get_top_scores(5)
        for i, entry in enumerate(top_scores, 1):
            print(f"{i}. {entry['Name']} - {entry['Score']} points")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print(f"\nGoodbye, {player.name}! Final score: {player.get_score()} points.")

if __name__ == "__main__":
    main()