# Example Game Functions Project, Jacob Desha, v0.5
import random

# Missing random.randint()  

# Game will be about punching, kicking, or headbutting an opponent until the opponent passes out, similar to rock, paper, scissors
# Variables
punch = False
kick = False
headbutt = False
hit = False
dodgeChance = 75
dodge = False
cpuDodge = False
health = 0
cpuHealth = 0
speed = 0
cpuSpeed = 0
cpuDodgeChance = 75
cpubodyType = ''
action = ''
bodyOption = ''
damage = 0
developerMode = False
isGameFinished = False
DM = ''

if developerMode == False:
    while isGameFinished == False
        if kick == True:
            damage = 20
        elif headbutt == True:
            damage = 30
        elif punch == True:
            damage = 15
        else:
            damage = 0


        

# Functions
def attack(act):
    global action, kick, headbutt, punch
    if developerMode == False:
        act = input('Would you like to punch, kick, headbutt, or dodge?')
        action = act.lower() 
        if action == action.startswith('k'):
            kick = True
            action = "Kick"
            print(f"You chose to {action}!")
        elif action == action.startswith('h'):
            headbutt = True
            action = "Headbutt"
            print(f"You chose to {action}!")
        elif action == action.startswith('p'):
            punch = True
            action = "Punch"
            print(f"You chose to {action}!")
        elif action == action.startswith('d'):
            action = "Dodge"
            print(f"You chose to {action}!")
    else: 
        act = input("Input what kind of attack you'd like to do!")
        while act == int(act):
            act = input("Input what kind of attack you'd like to do!")
        action = act.lower()

    # Player chooses attack option

def bodyType(body):
    global bodyOption, speed, health, dodgeChance, damage
    while bodyOption == '':
        if developerMode == False:
            body = input('What would you like your bodytype to be? Agile, Balanced, or Large?') # Body Types: Agile, Balanced, Bulky
            bodyOption = body.lower()
            bodyOption = bodyOption.lower()
            if bodyOption.startswith("a"):
                bodyOption = 'Agile'
                health = 50
                speed = 3
                dodgeChance = 25
                print(f"You chose {bodyOption}")
            elif bodyOption.startswith("b"):
                bodyOption = 'Balanced'
                health = 100
                speed = 2
                dodgeChance = 50
                print(f"You chose {bodyOption}")
            elif bodyOption.startswith("l"):
                bodyOption = 'Large'
                health = 150
                speed = 1
                dodgeChance = 75
                print(f"You chose {bodyOption}")
            else:
                print("Bodytype not available, please try again")
        else: 
            body = input("Input what kind of bodytype you would like to have")
            health = input("Type the amount of healthpoints you would like to have!")
            while health == str(health):
                health = input("Please input a number for the amount of health points you would like to have.")
            speed = input("Input the value you would like your speed to be!")
            while speed == str(speed):
                speed = input("Please input a number for the value you would like your speed to be.")
            dodgeChance = speed * 25
            damage = input("Input the amount of damage you would like to deal!")
            while damage == str(damage):
                damage = input("Please input a number for the amount of damage you would like to deal")

    
    # Player chooses body type at beginning of game

    # What value bodyType determines

def playerTurn(act): # Result of player's turn
    global cpuHealth, cpuDodge

    attack(act)

    if cpuDodge == True:
        print(f"You missed your {action}")
    else:
        cpuHealth -= damage
        print(f"You hit them with your {action} and did {damage} damage!")

    # elif action == "Kick" and kick == True and cpuDodge == False:
    #     cpuHealth -= damage
    #     print(f"You hit them with your {action} and did {damage} damage!")
    # elif action == "Heabutt" and headbutt == True and cpuDodge == False:
    #     cpuHealth -= damage
    #     print(f"You hit them with your {action} and did {damage} damage!")

    # elif action == "Punch" and punch == True and cpuDodge == False:
    #     cpuHealth -= damage
    #     print(f"You hit them with your {action} and did {damage} damage!")

    # Whether the player gets hit or not 

def cpu(cpuaction, cpuBody): # Result of cpu's turn
    global punch, kick, headbutt, cpuSpeed, cpuHealth, cpuDodgeChance, cpuDodge, action, cpubodyType
    while cpubodyType == '':
        if developerMode == False:
            cpubodyType = random.randint(1, 3)
            cpuaction = random.randint(1, 4)
            if cpubodyType == 3:
                cpubodyType = "Agile"
                cpuHealth = 50
                cpuSpeed = 3
                cpuDodgeChance = 25
            elif cpubodyType == 2:
                cpubodyType = "Balanced"
                cpuHealth = 100
                cpuSpeed = 2
                cpuDodgeChance = 50
            else:
                cpubodyType = "Fit"
                cpuHealth = 150
                cpuSpeed = 3
                cpuDodgeChance = 75
        else:
            cpuBody = input("Please input what kind of body you would like the cpu to have!")
            cpubodyType = cpuBody
            cpuBody = input("Please input what kind of body you would like the cpu to have!")
            cpuHealth = input("Type the amount of healthpoints you would like the cpu to have!")
            while cpuHealth == str(health):
                cpuHealth = input("Please input a number for the amount of health points you would like the cpu to have.")
                cpuSpeed = input("Input the value you would like the cpu's speed to be!")
            while cpuSpeed == str(speed):
                cpuSpeed = input("Please input a number for the value you would like the cpu's speed to be.")
            cpuDodgeChance = speed * 25
            damage = input("Input the amount of damage you would like to deal!")
            while damage == str(damage):
                damage = input("Please input a number for the amount of damage you would like to deal")

    if developerMode == False:
        cpubodyType = random.randint(1, 3)
        if cpuaction == 4:
            cpuaction = "Dodge"
        elif cpuaction == 3:
            kick = True
            cpuaction = "Kick"
        elif cpuaction == 2:
            headbutt = True
            cpuaction = "Headbutt"
        elif cpuaction == 1:
            punch = True
            cpuaction = "Punch"
    else: 
        act = input("Input what kind of attack you'd like the cpu to do!")
        while act == int(act):
            act = input("Input what kind of attack you'd like the cpu to do!")
        action = act.lower()


    # if speed == 3 and cpuDodgeChance < 51 and cpuaction == "Dodge":
    #     cpuDodge == False
    # elif speed == 2 and cpuDodgeChance < 26 and cpuaction == "Dodge":
    #     cpuDodge == False
    # elif speed == 1 and cpuDodgeChance > 0 and cpuaction == "Dodge":
    #     cpuDodge == True

def cpuTurn(cpuaction):
    global cpuDodge

    if speed < cpuDodgeChance / 25 and cpuaction == "Dodge":
        cpuDodge = True
    else:
        cpuDodge = False

    if cpuSpeed < dodgeChance / 25 and action == "Dodge":
        print(f"You dodged the {cpuaction}")
    else:
        print(f"You got hit with a {cpuaction} and took {damage} damage!")

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




    

    

bodyType(bodyOption)
attack(action)
playerTurn()