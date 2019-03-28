# Using lists
# The goal of this function is to take a list, and print it out as a sentence. 
# It will include proper grammar by separating individual items by a , and the last word will have an "and" put in front of it
def catList (userList):
    truncList = ""
    for i in range(0, len(userList)):
        if i == len(userList) -1:
            truncList += ", and " + userList[i]
        elif i == 0:
            truncList += userList[i]
        else:
            truncList += ", " + userList[i]
    return truncList

games = ['Mario Party', 'Legend Of Zelda', 'Metroid']
newList = catList(games)
print(newList)