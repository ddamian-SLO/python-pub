# Calculate Pi to the Nth number
# Program uses the Nilikantha Series to generate Pi. I am limiting it to 15 as the built in constat for Python is 15. 
# Pi is obviously already known. The goal was to generate Pi to a certain amount and not have to check it manually, even if it is added as a check. 
from decimal import Decimal, getcontext
import time, math
startTime = time.time()

# CONSTANTS
ADDITER = 2
getcontext().prec = 100

# SET VARS
piFifteenDigits = str(math.pi)
totalIter = 1
userIter = 0

# FUNCTIONS
def calcPi(iterations):
    pi = Decimal(3)
    step = 1
    for i in range(2, iterations * 2, 2):
        if step % 2 != 0:
            pi = pi + (Decimal(4) / (Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
            step += 1
        else:
            pi = pi - (Decimal(4) / (Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
            step += 1
    return str(pi)

# START PROGRAM
while userIter not in range(1, 11):
    try:
        print("How many decimal places of Pi would you like to return?\nYou can enter between numbers 1 and 10: ", end='')
        userIter = int(input())
    except:
        print("Error occurred. Please try again. ")
    else:
        if userIter == 0:
            print(f"0 is not a valid entry. Please try again. ")
        elif userIter > 10:
            print(f"10 is the maximum you can enter. Please enter a number between 1 and 10. ")
        else:
            print("You have selected " + str(userIter) + ". Beginning process.")

feedback = calcPi(ADDITER)
print(len(feedback))

# Slice the returned value at 2 instead of 0 so it matches the values after the decimal point so it doesn't match up to 3. 
while feedback[2:userIter + 2] not in piFifteenDigits:
    ADDITER += 1
    feedback = calcPi(ADDITER)
    totalIter += 1

print("Here is the result: " + feedback[0:userIter + 2])
print(f"It took {totalIter} iterations to complete this.")

endTime = time.time()
print("The script took " + str(endTime - startTime) + " to run.")