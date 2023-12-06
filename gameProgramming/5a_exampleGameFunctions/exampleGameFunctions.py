# Example Game Functions Project, Jacob Desha, v0.4
import random


# Game will be about punching, kicking, or headbutting an opponent until the opponent passes out, similar to rock, paper, scissors
# Variables
punch = False
kick = False
headbutt = False
hit = False
dodge = 75
health = 0
cpuHealth = 0
speed = 0
cpuSpeed = 0
action = ''
bodyOption = ''

# Functions
def attack(act):
    global action
    act = input('Would you like to punch, kick, or headbutt?')
    action = act.lower
    if action == action().startswith('k'):
        kick = True
        action = kick
    elif action == action().startswith('h'):
        headbutt = True
        action = headbutt
    elif action == action().startswith('p'):
        punch = True
        action = punch

    # Player chooses attack option

def bodyType(body):
    global bodyOption
    global speed
    global health

    body = input('What would you like your bodytype to be? Agile, Balanced, or Fit?') # Body Types: Agile, Balanced, Bulky
    bodyOption = body.lower
    if bodyOption == bodyOption().startswith('a'):
        body = 'Agile'
        bodyOption = body
        health = 50
        speed = 3
        dodge = 25
    elif bodyOption == bodyOption().startswith('b'):
        body = 'Balanced'
        bodyOption = body
        health = 100
        speed = 2
        dodge = 50
    elif bodyOption == bodyOption().startswith('f'):
        body = 'Fit'
        bodyOption = body
        health = 150
        speed = 3
        dodge = 75
    # Player chooses body type at beginning of game

    # What value bodyType determines

def playerTurn(body, speed, act): # Result of player's turn
    global action
    global bodyOption
    print(f'You chose {action}')
    print(f'You chose {bodyOption}')

    act = action
    body = bodyOption
    print(body)
    print(speed)
    print(act)

    # Whether the player gets hit or not 

def cpuTurn(cpubodyType, cpuDodge, cpuaction): # Result of cpu's turn
    pass
    if cpubodyType == 3:
        cpubodyType = "Agile"
        health = 50
        speed = 3
        cpuDodge = 25
    elif cpubodyType == 2:
        cpubodyType = "Balanced"
        health = 100
        speed = 2
        cpuDodge = 50
    else:
        cpubodyType = "Fit"
        health = 150
        speed = 3
        cpuDodge = 75

    if cpuaction == 3:
        kick = True
        cpuaction = kick
    elif cpuaction == 2:
        headbutt = True
        cpuaction = headbutt
    else:
        punch = True
        cpuaction = punch

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

attack(action)
bodyType(bodyOption)
playerTurn(action, speed, bodyOption)