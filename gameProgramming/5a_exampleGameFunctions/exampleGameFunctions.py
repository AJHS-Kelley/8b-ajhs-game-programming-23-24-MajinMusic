# Example Game Functions Project, Jacob Desha, v0.3
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
def attack(action = punch):
    pass
    action = input('Would you like to punch, kick, or headbutt?')
    action = action.lower
    if action == input().startswith('k'):
        kick = True
        action = kick
    elif action == input().startswith('h'):
        headbutt = True
        action = headbutt
    else:
        punch = True
        action = punch

    # Player chooses attack option

def bodyType(option):
    pass
    # Player chooses body type at beginning of game

    # What value bodyType determines

def Playerturn(bodyType, speed, action): # Result of player's turn
    print(f'You chose {action}')

    # Whether the player gets hit or not 

def cpuTurn(bodyType, speed, action): # Result of cpu's turn
    pass
    one = punch; two = kick; three = headbutt

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