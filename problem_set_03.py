def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    result = 0
    for i in range(int((stop - start)/step)):
        result += f(start + step*i)*step
    return result



# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/yaseru2003/Github/6001x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if len(secretWord) == 1 and secretWord in lettersGuessed:
        return True
    elif secretWord == '':
        return False
    else:
        return secretWord[0] in lettersGuessed and isWordGuessed(secretWord[1:], lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = {}
    for i in range(len(secretWord)):
        result[i] = '_ '
    if len(secretWord) == 1 and secretWord in lettersGuessed:
        result[0] = secretWord
        return result[0]
    elif len(secretWord) == 1 and secretWord not in lettersGuessed:
        return result[0]
    else:
        if secretWord[0] in lettersGuessed:
            result[0] = secretWord[0]
            return result[0] + getGuessedWord(secretWord[1:], lettersGuessed)
        else:
            return result[0] + getGuessedWord(secretWord[1:], lettersGuessed)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in lettersGuessed:
        if i in alpha:
            alpha = alpha.replace(i,"")
    return alpha    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    global lettersGuessed, count, update
    lettersGuessed = []
    count = 8
    update = '_ '*len(secretWord)
    #availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    def guess(secretWord):
        global lettersGuessed, count, update
        print "-----------"
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
        elif count == 0:
            print "Sorry, you ran out of guesses. The word was else."
        else:
            print 'You have ' + str(count) + ' guesses left.'
            print 'Available Letters: ' + getAvailableLetters(lettersGuessed)
            letter = raw_input('Please guess a letter: ')
            letter = letter.lower()
            if letter in lettersGuessed:
                print "Oops! You've already guessed that letter: " + update
                return guess(secretWord)
            elif len(letter) > 1:
                print "Please give just give me one letter. Try again: " + update
                return guess(secretWord)
            else:
                lettersGuessed.append(letter)

            if update == getGuessedWord(secretWord, lettersGuessed):
                count -= 1
                print "Oops! That letter is not in my word: " + update
                return guess(secretWord)
            else:
                update = getGuessedWord(secretWord, lettersGuessed)
                print "Good guess: " + update
                return guess(secretWord)
    return guess(secretWord)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print secretWord
hangman(secretWord)
