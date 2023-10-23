# Data Types and Operators, Jacob Desha, v0.7

# varaibale rules
#CANNOT START WITH A NUMBER !!!!!!!
# CANNOT USE BUILTY-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BE STORED.
# snake_case variables use _ to separate words, all lower case.
# camelCase variables do not use spaces, 1st word lower, rest uppercase.

# String Literal Examples
playerName = "Mega Man"
emptyString = ""
spaceString = " "
mapName = "Nuketown" 

# Inter Data Types
health = 100
extraLives = 5
temperature = -17
hunger = 98

# Floating Point Data Types
pi = 3.1415678
lapTime = 3.5
velocity = -2.0
mass=78.9

# Boolean Data Types
isFireType = False
weaponEquipped = True 
pvpEnabled = False
mapBanned = False 

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(4 + -5) # Addition
print(9 - 64) # Subtraction
print(2 * -2) # Multiplication
print(4 / -7) # Division
print(3 ** 4) # Exponents
print(7 % 68) # Modulus -- Divides the two numbers, then gives the remainder, most commonly used to determine even/odd

# Comparison Operators
# Evaluate the expression, then return True or False
print(10 > 7) # Greater Than
print(8 >= 4) # Greater Than or Equal to
print(2 < 12) # Less Than
print(9 <= 9) # Less Than or Equal to
print(30 == 30) # Is Equal to
print(-28 != 28) # Not Equal to

# Assignment Operators
myVariable = "myValue" # Assign variable on left the value on the right, throw out any current value
myOtherVariable = (10 + 5)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print( 3 > 5 and 4 < 3) # AND requires ALL expressions to be True.
print( 3 > 2 and 4 < 3)
print( 3 > 2 and 4 != 3)
print( 3 > 2 and 4 !=3 and mapName == "Nuketown" and temperature == -5)
# When writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires ONE expression to be True
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combineed
print("Line 81") 
print(3 > 2 and 4 < 3 or 5 != 7)
# print(True and False or True)

# NOT Logical Operator
print(not (3>2))
print(not (not (not (5!=3))))



