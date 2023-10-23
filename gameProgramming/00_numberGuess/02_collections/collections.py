# playerInventory = [] 

# while len(playerInventory)< 10:
#     item = input("What item do you want to add to the inventory?\n")
#     playerInventory.append(item)

# playerInventory.sort()
# print(playerInventory)

# while len(playerInventory) > 5:
#     item = input("What item do you want to remove from the inventory?\n")
#     playerInventory.remove(item)

# playerInventory.sort
# print(playerInventory)

# doorKeys = [
#     "red",
#     "blue",
#     "green",
#     "yellow",
#     "orange"
# ]

# key = input("Which color key do you need to unlock the door?\n")

# if key in dooryKeys:
#     print("You have the correct key! The door unlocks.\n")
# else:
#     print("You do not have that key. The door remains locked\n")

weaponList = [
    True, # Sword
    False, # Laser Gun
    False, # Railgun
    False, # Light Gun
    True, # Throwing Knives
    False, # Grenade Launcher
    True #Shrink Ray
]

weaponNum = 0
while weaponNum < len(weaponList):
    if weaponNum == 0 and weaponList[0] == True:
        print("You are wielding a shiny sword.\n")
    if weaponNum == 1 and weaponList[1] == True:
        print("You are wielding a Laser Gun\n")
    if weaponNum == 2 and weaponList[2] == True:
        print("You are wielding a giant Railgun\n")
    if weaponNum == 3 and weaponList[3] == True:
        print("You are wielding a dazzling Light Gun\n")
    if weaponNum == 4 and weaponList[4] == True:
        print("You are holding sharp Throwing Knives\n")
    if weaponNum == 5 and weaponList[5] == True:
        print("You are wielding a Grenade Launcher\n")
    if weaponNum == 6 and weaponList[6] == True:
        print("You are wielding a blue Shrink Ray\n")   
    weaponNum += 1