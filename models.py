class Player:
    def __init__(self, name):
        self.name = name
        self.__score = 0
    
    def add_points(self, points):
        if points > 0:
            self.__score += points
    
    def get_score(self):
        return self.__score

class GameWord:
    def __init__(self, word):
        self.word = word.upper()
        self.guessed_letters = set()
    
    def check_letter(self, letter):
        letter = letter.upper()
        if letter in self.word:
            self.guessed_letters.add(letter)
            return True
        return False
    
    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
    
    def is_fully_guessed(self):
        return all(letter in self.guessed_letters for letter in self.word)