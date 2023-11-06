# Hangman Game by Jacob Desha, v0.10
import random 
words = 'friend, great, world, king, dog, queen, fish, tiger, seven, apple, intervention, coordination, intellectual, xylophone, containment, continental, satelite, burdensome, enlightened, economy, philanthropist, appendicitis, pseudoscience, creationism, geriatrics, xenomophobic, hippopotomonstrosesquippedaliophobia, neuroscopic, incomprehensible, inconsequential'.split()
# DICTIONARY VERSION
# Stored in Key:Value Pairs.
#Actual Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary.
words = {'Colors': 'red orange yellow green blue indigo violet fuschia teal garnet gold black white silver'.split(),
          'Animals': 'cat cow dog moose goose fish wombat wolverine giraffe hippopotamus lion alligator'.split(),
          'Shapes': 'square triangle circle rhombus parallelogram trapezoid diamond dodecahedron'.split(),
          'Foods': 'hamburger hotdog potato waffle pancake escargot oysters chips steak'.split()}

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

def displayBoard(missedLetters, correctLetters, secretWord):
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
            blanks = blanks[:i] + secretWord[i] + blanks[i+1]
    
    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter.') 
        guess = input()
        guess = guess.lower()
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
    return input().lower().startswith('y')

# Introduce Game
print('Welcome to Hangman by Jacob Desha')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True: 
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check To See If Winner, Winner Chicken Dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False 
                break
        if foundAllLetters: #if True:
                print('You won... Haray...')
                print('The secret word was' + secretWord)
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD):
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('You made this number of correct guesses ', str(len(missedLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True

    if gameIsDone: 
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break

# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1


