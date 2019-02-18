# This is a basic example creating a variable that holds an int, convert to str, then concatenate, then print.


# The following fails because you cannot concatenate 
# a string and an integer. You must convert the integer into a string first

# age = 21
# message = "Happy " + age + "st Birthday!"

# print(message)

age = 21 
message = "Happy " + str(age) + "st Birthday!"
print(message)

