# Dice Rolling Module by Jacob Desha, v0.2
import random 

def roll(numDice, sizeDice): # Verified Working 12-14-23
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        numRolled += 1
    return sum # return will IMMEDIATELY exit a loop, function, if/elif/else block.

def display(numDice, sizeDice): # Verified Working 12-14-23
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
    return sum # return will IMMEDIATELY exit a loop, function, if/elif/else block.

def isDoubles(roll1, roll2): # Verified Working 12-14-23
    if roll1 == roll2:
        isDoubles = True
    else:
        isDoubles = False
    return isDoubles