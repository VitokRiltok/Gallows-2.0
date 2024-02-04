import os
import sys
from libhangman.hangman import HangmanGame


def show_menu():
    print("1. Новая игра")
    print("2. Выбрать букву")



def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        print('\033c', end='')


def main():
    word_list = ["никитос", "чушпан", "крем", "тауматафакатангихангакоауауотаматеатурипукакапикимаунгахоронукупокаифенуакитанатаху", "солнце"]
    max_guesses = 6

    game = HangmanGame(word_list, max_guesses)

    while True:
        if game.in_progress:
            game.display_word()
            print("\nПопыток: " + str(game.guesses_left) +
                  "/" + str(max_guesses))

        show_menu()
        choice = input("Нажмите (1/2): ")

        if choice == "1":
            os.system('clear')
            game.start_game()
            clear_console()
        elif choice == "2":
            os.system('clear')
            if game.in_progress:
                letter = input("Введите букву: ").lower()
                game.make_guess(letter)
                clear_console()
            else:
                print("Игра не начата. Начните новую игру сначала.")
        elif choice == "0":
            print("шампунь жумайсынба")
            break
        else:
            print("Неверный выбор. Введите 1 или 2.")


if __name__ == "__main__":
    main()


