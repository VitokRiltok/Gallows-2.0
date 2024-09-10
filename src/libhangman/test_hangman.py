import unittest
from hangman import HangmanGame  # Предположим, что ваш код сохранён в файле hangman.py
import random

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        self.word_list = ["python", "hangman", "test"]
        self.game = HangmanGame(self.word_list)

    def test_start_game(self):
        self.game.start_game()
        self.assertIn(self.game.secret_word, self.word_list)
        self.assertEqual(self.game.guesses_left, self.game.max_guesses)
        self.assertTrue(self.game.in_progress)

    def test_display_word_initial(self):
        self.game.start_game()
        display = self.game.display_word()
        self.assertEqual(display, "_" * len(self.game.secret_word))

    def test_make_guess_correct(self):
        self.game.start_game()
        letter = self.game.secret_word[0]  # Предполагаем, что первая буква - правильная
        self.game.make_guess(letter)
        display = self.game.display_word()
        self.assertIn(letter, display)

    def test_make_guess_incorrect(self):
        self.game.start_game()
        incorrect_letter = 'z'  # Предполагаем, что 'z' не в слове
        initial_guesses_left = self.game.guesses_left
        self.game.make_guess(incorrect_letter)
        self.assertEqual(self.game.guesses_left, initial_guesses_left - 1)

    def test_make_guess_already_guessed(self):
        self.game.start_game()
        letter = self.game.secret_word[0]
        self.game.make_guess(letter)  # Первое угадывание
        initial_guesses_left = self.game.guesses_left
        self.game.make_guess(letter)  # Повторное угадывание
        self.assertEqual(self.game.guesses_left, initial_guesses_left)

    def test_game_win_condition(self):
        self.game.word_list = ["a"]
        self.game.start_game()
        for letter in self.game.secret_word:
            self.game.make_guess(letter)
        self.assertFalse(self.game.in_progress)

    def test_game_loss_condition(self):
        self.game.word_list = ["abc"]
        self.game.start_game()
        for _ in range(self.game.max_guesses):
            self.game.make_guess('z')  # Угадываем неправильные буквы
        self.assertFalse(self.game.in_progress)

if __name__ == '__main__':
    unittest.main()
