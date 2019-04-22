# Define Dict
playerInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(itemDict):
    totalInventory = 0

    print("Inventory:")
    for key, value in itemDict.items():
        print( str(value) + " " + key)
        totalInventory += value
    print("Total number of items in your inventory: " + str(totalInventory))

def addToInventory(itemDict, addedItemsList):
    for item in addedItemsList:
        itemDict.setdefault(item, 0)
        itemDict[item] = itemDict[item] + 1

displayInventory(playerInventory)
addToInventory(playerInventory, dragonLoot)
displayInventory(playerInventory)