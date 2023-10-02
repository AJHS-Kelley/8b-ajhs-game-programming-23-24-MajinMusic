# Collections Examples, Jacob Desha, v0.5a

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
#breakfastFoods.append("Banana")
#print(breakfastFoods)
#testScores.append(57)
#print(testScores)
#classGPA.append(3.341)
#print(classGPA)

# Deleting Items from a List
# Use .remove() to remove a specific item from the list.
#breakfastFoods.remove("Pancakes")
#print(breakfastFoods)
#testScores.remove(100)
#print(testScores)
#classGPA.remove(2.25)
#print(classGPA)

# To delete using the index value we use .pop()
#breakfastFoods.pop(4)
#print(breakfastFoods)
#testScores.pop(4)
#print(testScores)
#classGPA.pop(4)
#print(classGPA)

# PAUSE - WYOC -- .pop() the 2nd element from each list.  .remove() any item from the list.
#breakfastFoods.remove("Eggs")
#print(breakfastFoods)
#testScores.remove(25)
#print(testScores)
#classGPA.remove(1.74)
#print(classGPA)

# Determining List Length
#print(f"There are {len(breakfastFoods)} items in the breakfastFoods list.")
#print(f"There are {len(testScores)} items in the testScores list.")
#print(f"There are {len(classGPA)} items in the classGPA list.")

# List Methods -- Functions for working with lists.
# Sorting Lists -- Aplhanumerical -- Ascending -- Capital Letters before Lower Cases Letters
#print(f"The original breakfastFoods list is {breakfastFoods}.")
#breakfastFoods.sort()
#print(f"The sorted breakfastFoods list is {breakfastFoods}.")
#print(f"The original breakfastFoods list is {testScores}.")
#testScores.sort()
#print(f"The sorted breakfastFoods list is {testScores}.")
#print(f"The original breakfastFoods list is {classGPA}.")
#classGPA.sort()
#print(f"The sorted breakfastFoods list is {classGPA}.")


breakfastFoods = ["Bacon", "Eggs", "Cereal", "Pancakes", "Milk", "Milk"]
testScores = [95, 100, 25, 15, 27, 35, 100]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25, 4.25]

# .count() will return the number of times a value appears in a list.
#numMilk = breakfastFoods.count("Milk")
#print(f"There are {numMilk} Milks in the list.")
#numPancakes = breakfastFoods.count("Pancakes")
#print(f"There are {numPancakes} Pancakes in the list.")
# Pause -- WYOC -- Use .count() to count for a single item in the list and any multiple items. Use testSxores and classGPA.
#testCount = testScores.count(100)
#print(f"There was {testCount} perfect 100 scores.")
#testCount15 = testScores.count(15)
#print(f"There was {testCount15} 15 scores.")
#gpaCount = classGPA.count(1.99)
#print(f"There is {gpaCount} GPA equal to 1.99")
#gpaCountRepeat = classGPA.count(4.25)
#print(f"There is {gpaCountRepeat} GPA equal to 4.25")

# Deleting All Contents of a List -- .clear()
#breakfastFoods.clear()
#print(f" The breakfast foods list is {breakfastFoods}.")
#testScores.clear()
#print(f" The testScores list is {testScores}.")
#classGPA.clear()
#print(f" The classGPA list is {classGPA}.")

# Common Bugs -- Index Out of Range
print(f"The last item in the list is {breakfastFoods[4]}.")

print(f" The last item in the teastScores list is {testScores[len(testScores) - 1]}.")