playerInventory = [] 

while len(playerInventory)< 10:
    item = input("What item do you want to add to the inventory?\n")
    playerInventory.append(item)

playerInventory.sort()
print(playerInventory)