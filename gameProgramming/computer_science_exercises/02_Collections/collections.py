# Collections Examples, Jacob Desha, v0.2a

# LIST -- ORDERED, CHANGEAVLE, ALLOWS DUPLICATE VALUES\
breakfastFoods = ["Bacon", "Eggs", "Cereal", "Pancakes", "Milk"]
# Each itom on the list is known as an ELEMENT.
# The position in the list for each is the INDEX.
# The element "BACON" is at index 0.
# Python Only: index -1 is the last itom on the list.
testScores = [95, 100, 25, 15, 27, 35]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

# Printing Contents of a List
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

# Accessing Specific List Elements -- REMEMBER FIRST ELEMENT IS INDEX 0
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])

# Accessing Last Element in Lists
#print(breakfastFoods[-1])
#print(testScores[-1])
#print(classGPA[-1])

# Pause - WYOC -- Access the 3rd Element in Each Lis
#print(breakfastFoods[2])
#print(testScores[2])
#print(classGPA[2])

# Changing Items in a List
#breakfastFoods[0] = "Sausage"
#testScores[0] = 97
#classGPA[0] = 3.75
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

# Pause -- WYOC -- Change 5th Element
#breakfastFoods[4] = "Bagel"
#testScores[4] = 45
#classGPA[4] = 2.45
#print(breakfastFoods)
#print(testScores)
#print(classGPA)
# Adding and Inserting Items to a List
# .append90 adds an item to the END of a list.
#breakfastFoods.append("Hash Browns")
#print(breakfastFoods)
#testScores.append(99)
#print(testScores)
#classGPA.append(1.99)
#print(classGPA)

# .insert() allows you to place an item at a specific index in the list
#breakfastFoods.insert(3, "Parfait")
#print(breakfastFoods)
#testScores.insert(3, 55)
#print(testScores)
#classGPA.insert(3, 0.0)
#print(classGPA)

# PAUSE -- WYOC -- .append() another item to each list. .insert() an item at index 5 to each list.
breakfastFoods.append("Banana")
print(breakfastFoods)
testScores.append(57)
print(testScores)
classGPA.append(3.341)
print(classGPA)
