# test
todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
 {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'},
 {'name': 'Task 3', 'body': 'Third task', 'points': '5'}]

totalPoints = 0
for i in range(len(todos)):
    totalPoints += int(todos[i]['points'])
print(str(totalPoints))