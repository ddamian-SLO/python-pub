# Re-sort list containing lists
import copy
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Function takes a list and will resort the list to basically flip it 90 degrees to the right. 
# As of now there is no error checking. This requires a list passed to the function to have a list in each index. 
def reSortList(userList):
    newList = []
    
    for i in range(0, len(userList[0])):
        newList.append([])
        for j in range(0, len(userList)):
            newList[i].append(copy.deepcopy(userList[j][i]))
            print(newList[i][j], end='')
        print('')
    return newList

brandNewGrid = reSortList(grid)