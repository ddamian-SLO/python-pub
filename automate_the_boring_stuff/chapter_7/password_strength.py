# Strong Password Detection

# Function will detect password strength. Password must be 
# 8 characters long
# Contain capital and lower case letters
# Contains a digit
import re, sys

def passwdStrength(password):
    if len(password) < 8:
        return f'Password does not meet the length requirements.'
    
    pass_strength_upper_regex = re.compile(r'[A-Z]')
    pass_strength_lower_regex = re.compile(r'[a-z]')
    pass_strength_number_regex = re.compile(r'[0-9]')

    try:
        if pass_strength_upper_regex.findall(password) != []:
            print('Upper case letter found in password.')
        else:
            return f'Password does not contain an uppercase letter.'
        
        if pass_strength_lower_regex.findall(password) != []:
            print('Lower case letter found in password.')
        else:
            return f'Password does not contain a lowercase letter.'
        
        if pass_strength_number_regex.findall(password) != []:
            print('Number found in password.')
        else:
            return f'Password does not contain a number.'
    except:
        print('General error occurred')
        return f'Error has occurred.'

    return f'Password is valid.'

def main():
    print('Please enter your password: ', end='')
    get_passwd = input()
    print('Checking password...')
    print(passwdStrength(get_passwd))

###     RUN     ###
main()
###     STOP    ###