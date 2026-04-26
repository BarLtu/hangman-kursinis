from abc import ABC, abstractmethod
import random

class WordSource(ABC):
    @abstractmethod
    def get_word(self):
        pass

class ListWordSource(WordSource):
    def __init__(self, words):
        self.__words = ["Object", "Oriented", "Programming", "Language", "Python"]

    def get_word(self):
        return random.choice(self.__words)
        
class FileWordSource(WordSource):
    def __init__(self, filename = "words.txt"):
        self.file_path = filename

    def get_word(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                words = file.readlines()
                if not words:
                    return "FALLBACK"
                return random.choice(words).strip().upper()
        except FileNotFoundError:
            return "PYTHON"
        