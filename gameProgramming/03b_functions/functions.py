import random
# FUNCTION -- a named piece of code that can be reused easily.
# FUNCTION SIGNATURE -- Syntax for creating aexm new function.
def exampleFunctionA(): # NO PARAMETERS
    count = 0
    num = int(input("How many times do you want to wish a happy birthday?\n"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1

def exampleFunctionB(num, count): # PARAMETERS
    while count < num:
        print("Happy Birthday!\n")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION!
# exampleFunctionA()
# exampleFunctionB(5, 0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
    return sum

rollDice(5, 7)
rollDice(6, 10)

strengthPlayer = rollDice(3, 6)
dexterityPlayer = rollDice(3, 6)
wisdomPlayer = rollDice(3, 6)

print(strengthPlayer)
print(dexterityPlayer)
print(wisdomPlayer)



