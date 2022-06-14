#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:18:35 2022

@author: chichi_ry
"""

# Problem Set 2, hangman.py
# Name: Ryan Chironga
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_list = list(secret_word)
    
    for a in letters_guessed:
        if a in secret_word_list:
            while a in secret_word_list:
                secret_word_list.remove(a)
    if len(secret_word_list) == 0:
        return True
    else:
        return False


def is_word_guessed(secret_word, letters_guessed):    
    pass
    secret_word_list = list(secret_word)
    secret_word_list_copy = secret_word_list[:]
    
    for a in secret_word_list:
        if a in letters_guessed:
            while a in secret_word_list_copy:
                secret_word_list_copy.remove(a)
    if len(secret_word_list_copy) == 0:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_list = list(secret_word)
    word_guessed = []
    
    for b in secret_word_list:
        if b in letters_guessed:
            word_guessed.append(b)
        else:
            word_guessed.append("_ ")
    word_returned = ''.join(word_guessed)
    return word_returned


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_list = list(string.ascii_lowercase)
    for c in letters_guessed:
        if c == '*':
            continue
        else:
            letters_list.remove(c)
    return ''.join(letters_list)
    

def is_letter_guessed(secret_word, letter_guessed):
    secret_word_list = list(secret_word)

    if letter_guessed in secret_word_list:
        return True
    else:
        return False
    
    
def unique_letters(secret_word):
    unique_letter_count = []
    
    for d in secret_word:
        if d not in unique_letter_count:
            unique_letter_count.append(d)
    return (len(unique_letter_count))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    letters_guessed = []
    guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secret_word), 'letters long.')
    print('-------------\nYou have', warnings, 'warnings left.')
    while (is_word_guessed(secret_word, letters_guessed) == False and guesses > 0):
        print('-------------\nYou have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        letter_guessed = str(input('Please guess a letter: '))
        if letter_guessed in string.ascii_letters:
            if str.isalpha(letter_guessed):
                str.lower(letter_guessed)
            if letter_guessed not in get_available_letters(letters_guessed):
                if warnings > 0:
                    warnings -= 1
                    print("Oops! You've already guessed that letter. You have", warnings, "warnings left.")
                else:
                    guesses -= 1
                    print("Oops! You've already guessed that letter but you are out of warnings. So you lose a guess.")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(letter_guessed)
                if is_letter_guessed(secret_word, letter_guessed) == True:
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                else:
                    if letter_guessed in vowels and guesses >= 2:
                        guesses -= 2
                    else:
                        guesses -= 1
                    print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        else:
            if warnings > 0:
                warnings -= 1
                print('Oops! That is not a valid letter. You have', warnings, 'warnings left.')
            else:
                guesses -= 1
                print("Oops! You've already guessed that letter but you are out of warnings. So you lose a guess.")
            print(get_guessed_word(secret_word, letters_guessed))
    
    print('-----------')
    if guesses == 0:
        print('Sorry, you ran out of guesses. The word was', secret_word + '.')
    else:
        print('Congratulations, you won!')
        print('Your total score for this game is:', (unique_letters(secret_word) * guesses))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    length = 0
    counter = 0
    while counter < len(my_word):
        if my_word[counter] == '_':
            if other_word[counter] in my_word:
                counter += 1
            else:
                counter += 1
                length += 1
        if my_word[counter] == other_word[counter]:
            length += 1
            counter += 1
        else:
            counter +=1
    
    if length == counter:
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = list(my_word)
    for e in guessed_word:
        if e == ' ':
            guessed_word.remove(' ')

    number_of_matches = 0
    possible_matches = []
    
    for f in wordlist:
        if len(f) == len(guessed_word):
            if match_with_gaps(guessed_word, f) == True:
                possible_matches.append(f)
                number_of_matches += 1
            else:
                continue
        else:
            continue

    if number_of_matches <= 0:
        print('No matches found.')
    else:
        print('Possible word matches are:')
        print(' '.join(possible_matches))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses = 6
    warnings = 3
    guess_number = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secret_word), 'letters long.')
    print('-------------\nYou have', warnings, 'warnings left.')
    while (is_word_guessed(secret_word, letters_guessed) == False and guesses > 0):
        print('-------------\nYou have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        letter_guessed = str(input('Please guess a letter: '))
        if guess_number < 1 and letter_guessed == "*":
            print("That's terrible. I'll give you 55,900 words if you ask for a hint now. Try again first.")
            continue
        if letter_guessed in string.ascii_letters or letter_guessed == '*':
            guess_number += 1
            if letter_guessed == '*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            if str.isalpha(letter_guessed) == True:
                letter_guessed = str.lower(letter_guessed)
            if letter_guessed not in get_available_letters(letters_guessed):
                if letter_guessed == '*':
                    continue
                if warnings > 0:
                    warnings -= 1
                    print("Oops! You've already guessed that letter. You have", warnings, "warnings left.")
                else:
                    guesses -= 1
                    print("Oops! You've already guessed that letter, but you are out of warnings. So you lose a guess.")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(letter_guessed)
                if is_letter_guessed(secret_word, letter_guessed) == True:
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                else:
                    if letter_guessed in vowels and guesses >= 2:
                        guesses -= 2
                    else:
                        guesses -= 1
                    print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        else:
            if warnings > 0:
                warnings -= 1
                print('Oops! That is not a valid letter. You have', warnings, 'warnings left.')
            else:
                guesses -= 1
                print("Oops! That is not a valid letter, but you are out of warnings. So you lose a guess.")
            print(get_guessed_word(secret_word, letters_guessed))
    
    print('-----------')
    if guesses == 0:
        print('Sorry, you ran out of guesses. The word was', secret_word + '.')
    else:
        print('Congratulations, you won!')
        print('Your total score for this game is:', (unique_letters(secret_word) * guesses))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # secret_word = 'bridging'
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)