# Hangman Game by Jacob Desha, v0.1

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
