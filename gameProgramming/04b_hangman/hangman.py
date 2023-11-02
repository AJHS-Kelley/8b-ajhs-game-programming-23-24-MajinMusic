# Hangman Game by Jacob Desha, v0.4
import random 
words = 'friend, great, world, king, dog, queen, fish, tiger, seven, apple, intervention, coordination, intellectual, xylophone, containment, continental, satelite, burdensome, enlightened, economy, philanthropist, appendicitis, pseudoscience, creationism, geriatrics, xenomophobic, hippopotomonstrosesquippedaliophobia, neuroscopic, incomprehensible, inconsequential'.split()

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
     =======''', '''
    +---+
    o   |
        |
        |
     =======''', '''
    +---+
    o   |
    |   |
        |
     =======''', '''
    +---+
    o   |
   /|   |
        |
     =======''', '''
    +---+
    o   |
   /|\  |
        |
     =======''', '''
    +---+
    o   |
   /|\  |
   /    |
     =======''', '''
    +---+
    o   |
   /|\  |
   / \  |
     =======''']

# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord)
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()

    blanks = '_' * len(secretWord)
    # Replace blaks with Correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[i] + secretWord[i] + blanks[i+1]
    
    for letter in blankss:
        print(letter, end = ' ')
    print()
# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1


