import random
import os

class HangmanGame:
    def __init__(self, word_list, max_guesses=6):
        self.is_debug = False
        self.word_list = word_list
        self.secret_word = ""
        self.max_guesses = max_guesses
        self.guesses_left = max_guesses
        self.guesses = set()
        self.in_progress = False

    def start_game(self):
        self.secret_word = random.choice(self.word_list)
        self.guesses_left = self.max_guesses
        self.guesses = set()
        self.in_progress = True
        self.display_word()

    def display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        print(display)
        return display

   