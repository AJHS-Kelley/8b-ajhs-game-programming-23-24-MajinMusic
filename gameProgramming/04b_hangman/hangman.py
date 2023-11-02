# Hangman Game by Jacob Desha, v0.8
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


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter.') 
        guess = input()
        guess = guess.lower
        if len(guess) != 1:
            print('Enter a single letter')
        elif guess in alreadyGuessed:
            print('Silly lil guy, you already guessed that letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English alphabet.')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswitch('y')

# Introduce Game
print('Welcome to Hangman by Jacob Desha')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True: 
    displayBoard(missedLeters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess


# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1


