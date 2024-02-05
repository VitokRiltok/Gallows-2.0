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

    def make_guess(self, letter):
        if not self.in_progress:
            print("Игра ещё не началась.")
            return

        if letter in self.guesses:
            print("Вы уже выбирали этот символ.")
            return

        self.guesses.add(letter)

        if letter not in self.secret_word:
            self.guesses_left -= 1
            print(
                "Увы, такой буквы нет.\nОсталось попыток: " +
                str(self.guesses_left))

        # self.display_word()

        guessed_word = "".join(
            [letter if letter in self.guesses
             else "_" for letter in self.secret_word])
        is_word_guessed = guessed_word == self.secret_word

        if is_word_guessed:
            self.in_progress = False
            os.system('cls')
            print("Ура,победа,победа:", self.secret_word)
        elif self.guesses_left == 0:
            self.in_progress = False
            print("Жаль.., но вы проиграли.. Эй, ребята, снимите-ка с него шкуру. Верное лово:", self.secret_word)

        if not self.is_debug:
            input("Для продолженя нажмите Enter...")
