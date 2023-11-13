# Example Game Functions Project, Jacob Desha, v0.2
import random


# Game will be about punching, kicking, or headbutting an opponent until the opponent passes out, similar to rock, paper, scissors
# Variables
punch = False
kick = False
headbutt = False
hit = False
dodge = False
health = 0
cpuHealth = 0
speed = 0
cpuSpeed = 0

# Functions
def attack(action):
    pass
    # Player chooses attack option

def bodyType(option = 1):
    pass
    # Player chooses body type at beginning of game

    # What value bodyType determines

def Playerturn(bodyType, speed, action): # Result of player's turn
    pass

    # Whether the player gets hit or not 

def cpuTurn(bodyType, speed, action): # Result of cpu's turn
    pass

    # Whether the player gets hit or not


# Example of working Function
# def catchBall(throwQuality, passCatchScore, weather):
#     if throwQuality > 5.0 and passCatchScore >= 99 and weather == 'Sunny':
#         ballCaught = True
#     elif throwQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
#         ballCaught = False
#     else:
#         print('Oh, no, interception!\n')
#         ballIntercepted = True
#         return ballIntercepted
#     return ballCaught

# catchBall(4.25, 107, 'Rainy')