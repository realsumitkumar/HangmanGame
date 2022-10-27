import random
import string

from Words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the words
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has entered till now

    lives = 10  # the user has limited chance of 10
    # getting input from the user
    while len(word_letters) > 0 and lives > 0:
        # show what the user has entered till now
        print('you have', lives, 'lives left and you have used these letter : ', ' '.join(used_letters))
        # show the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('the current word is : ', ' '.join(word_list))

        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # a chance is taken for wrong answer

        elif user_letter in used_letters:
            print('you already entered this alphabet before ,enter again')
        else:
            print('Invalid alphabet, enter again')

    if lives == 0:
        print('sorry you lost, the word was ', word)
    else:
        print('Yeah you guess the word ', word, '!')


hangman()
