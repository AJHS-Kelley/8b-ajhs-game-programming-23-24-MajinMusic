# Example Game Functions Project, Jacob Desha, v0.7
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
DM = ''# Generally, an all-caps name means the variable is a CONSTANT. 
cpuaction = 0
resume = ''
cpudamage = 0



def checkScaling():
    global damage
    if developerMode == False: #Determines Damage For Attacks if NOT in Developer Mode
            if isGameFinished == False:
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
    global action, kick, headbutt, punch, damage
    if developerMode == False:
        act = input('Would you like to punch, kick, headbutt, or dodge?\n')
        action = act.lower() 
        if action.startswith('k'):
            kick = True
            action = "Kick"
            print(f"You chose to {action}!")
        elif action.startswith('h'):
            headbutt = True
            action = "Headbutt"
            print(f"You chose to {action}!")
        elif action.startswith('p'):
            punch = True
            action = "Punch"
            print(f"You chose to {action}!")
        elif action.startswith('d'):
            action = "Dodge"
            damage = 0
            print(f"You chose to {action}!")
        
    else: 
        act = input("Input what kind of attack you'd like to do!")
        action = act.lower()

    # Player chooses attack option

def bodyType(body):
    global bodyOption, speed, health, dodgeChance, damage
    if developerMode == False:
        while bodyOption == '':
            body = input('What would you like your bodytype to be? Agile, Balanced, or Large?') # Body Types: Agile, Balanced, Bulky
            bodyOption = body.lower()
            bodyOption = bodyOption.lower()
            if bodyOption.startswith("a"):
                bodyOption = 'Agile'
                health = 50
                speed = 3
                dodgeChance = 75
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
                dodgeChance = 25
                print(f"You chose {bodyOption}")
            else:
                print("Bodytype not available, please try again")
    else: 
        body = input("Input what kind of bodytype you would like to have")
        bodyOption = body
        health = int(input("Type the amount of healthpoints you would like to have!"))
        speed = int(input("Input the value you would like your speed to be!"))
        dodgeChance = speed * 25
        damage = int(input("Input the amount of damage you would like to deal!"))
    
    # Player chooses body type at beginning of game

    # What value bodyType determines

def playerTurn(action): # Result of player's turn
    global cpuHealth, cpuDodge, damage

    if developerMode == False: #Determines Damage For Attacks if NOT in Developer Mode
        if isGameFinished == False:
            if kick == True:
                damage = 20
            elif headbutt == True:
                damage = 30
            elif punch == True:
                damage = 15
            else:
                damage = 0
    
    if speed < cpuDodgeChance / 25 and cpuaction == "Dodge":
        cpuDodge = True
    else:
        cpuDodge = False

    if cpuDodge == True:
        print(f"You missed your {action}")
    elif action == "Dodge":
        cpuHealth -= damage
        print(f"You decided to {action}!")
    else:
        cpuHealth -= damage
        print(f"You hit them with a {action} and did {damage} damage!")

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

def cpu(cpuBody): # Result of cpu's turn
    global punch, kick, headbutt, cpuSpeed, cpuHealth, cpuDodgeChance, cpuDodge, action, cpubodyType, cpudamage
    if developerMode == False:
        cpubodyType = random.randint(1, 3)
        if cpubodyType == 3:
            cpubodyType = "Agile"
            cpuHealth = 50
            cpuSpeed = 3
            cpuDodgeChance = 75
        elif cpubodyType == 2:
            cpubodyType = "Balanced"
            cpuHealth = 100
            cpuSpeed = 2
            cpuDodgeChance = 50
        else:
            cpubodyType = "Large"
            cpuHealth = 150
            cpuSpeed = 1
            cpuDodgeChance = 25
    else:
        cpuBody = input("Please input what kind of body you would like the cpu to have!")
        cpubodyType = cpuBody
        cpuHealth = int(input("Type the amount of healthpoints you would like the cpu to have!"))
        cpuSpeed = int(input("Input the value you would like the cpu's speed to be!"))
        cpuDodgeChance = speed * 25
        cpudamage = int(input("Input the amount of damage you would like the cpu to deal!"))


    # if speed == 3 and cpuDodgeChance < 51 and cpuaction == "Dodge":
    #     cpuDodge == False
    # elif speed == 2 and cpuDodgeChance < 26 and cpuaction == "Dodge":
    #     cpuDodge == False
    # elif speed == 1 and cpuDodgeChance > 0 and cpuaction == "Dodge":
    #     cpuDodge == True

def cpuTurn(cpuaction):
    global cpuDodge, kick, headbutt, punch, damage, health
    if developerMode == False:
        cpuaction = random.randint(1, 3)
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
        cpuaction = input("Input what kind of attack you'd like the cpu to do!")
        cpuaction.lower()

    if developerMode == False: #Determines Damage For Attacks if NOT in Developer Mode
        if isGameFinished == False:
            if kick == True:
                damage = 20
            elif headbutt == True:
                damage = 30
            elif punch == True:
                damage = 15
            else:
                damage = 0

    if speed < cpuDodgeChance / 25 and cpuaction == "Dodge":
        cpuDodge = True
    else:
        cpuDodge = False

    if cpuSpeed < dodgeChance / 25 and action == "Dodge":
        print(f"You dodged the Cpu's {cpuaction}!\n \n \n")
    else:
        print(f"You got hit with a {cpuaction} and took {damage} damage!\n \n \n")
        health -= damage

    if developerMode == False:
        if cpuSpeed < dodgeChance / 25 and action == "Dodge":
            print(f"You dodged the Cpu's {cpuaction}!\n \n \n")
        else:
            print(f"You got hit with a {cpuaction} and took {damage} damage!\n \n \n")
            health -= damage


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


while isGameFinished == False:
    print("Welcome to The Fighter!\n \n")
    DM = input("Would you like to play in developer mode? Y or N?").lower()
    if DM.startswith("y"):
        developerMode = True
    else:
        developerMode = False

    bodyType(bodyOption)
    cpu(cpuBody = '')
    print("Now that you have chosen your options, Lets Start!\n \n \n")

    while cpuHealth > 0 and health > 0:
        print(f"Cpu has {cpuHealth} health points\nYou have {health} health points")
        print(f"The Cpu's bodytype is {cpubodyType}\nYour bodytype is {bodyOption}")
        attack(action)
        playerTurn(action)
        cpuTurn(cpuaction)
        if health <= 0 and cpuHealth > health:
            print("You ran out of health and died!")
            resume = input("Would you like to play again?\n")
            if resume.startswith("y"):
                print("\n\n\n\n")
                break
            else:
                isGameFinished = True
                break
                    



    

    

    

