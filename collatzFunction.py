# The Collatz Sequence


# define function:
#     check if number provided by user is even by checking its remainder
#     if the remainder is equal to 0
#         then print and return the number divided by 2
#     if the remainder is equal to 1
#         then print and return the number multiplied by 3 and add 1
#     else
#         print invalid number and return None 

# To determine if something is odd or even, use remainders. Evens will never have remainders, odds will always have remainders. 
def collatz(number):
    
    remainder = number % 2

    if remainder == 0:
        number = number // 2
        print(str(number))
        return number

    elif remainder == 1:
        number = 3 * number + 1
        print(str(number))
        return number

    else: 
        print('Something weird happened')
        return None

# Track increments and report it later
increments = 0

print('Welcome to the Collatz Sequence Example. Enter in a number (please) and watch it calculate down to 1.')
print('Enter your number: ', end='')

# If the user inputs something not an integer, it keeps them in this loop
# I want to return to this to figure out how to break this while loop without a break statement
while True:
    try:
        answer = int(input())
        break
    except ValueError:
        print('You entered something that is not an integer. Please enter a number: ')

# Joke, not needed
if answer == 1:
    print("Well it's already 1 so good job")

# If it is equal to 1, it will end the loop and stop running the collatz sequence.
while answer != 1:
    answer = collatz(answer)
    increments += 1

print("It took " + str(increments) + " iterations to get to 1!")