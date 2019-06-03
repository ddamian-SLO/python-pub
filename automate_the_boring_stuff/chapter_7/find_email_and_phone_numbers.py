# Find all email addresses and phone numbers by copying them.
# Flow of program:
# - Pull text copied on the clipboard
# - Find all the phone numbers and email addresses in the text
# - Paste the text back onto the clipboard
# Phone number is made of three parts, 
# (111) 111-1111
# 123-456-7890
# Area code separated by a dash at the end or encapsulated by parentheses, 
# 3 digits separated with a dash at the end, 
# and then 4 digits
# Regex will need to detect:
#   The area code and it's different separators
#   The separator after the area code (either space or a dash)
#   The 3 digits
#   The separator again
#   The 4 digits

# An email address is made of 2 parts: 
#   name@domain.com
#   Regex will need to check for:
#       - The name before the '@' sign.
#       - The @ sign
#       - The full domain (including the subdomain. It should just be able to check if it ends with a character)
# Things to consider:
#   email addresses often have underscores or periods(.)
#   email addresses cannot start with a special character
#   the account name ends when it reaches @
#   the domain begins after the @ symbol
#   The domain ends once it reaches it's TLD
#   The TLD has to end with a string

import re, pyperclip

def searchClipboard(regExPhone, regExEmail, inputText):
    '''
    Function used to search text with specified regex objects and return
    a list of phone numbers and email addresses. 
    '''
    matches = []
    regExPhoneList = regExPhone.findall(inputText)
    regExEmailList = regExEmail.findall(inputText)

    for group in range(len(regExPhoneList)):
        phoneNumber = '-'.join([regExPhoneList[group][1], regExPhoneList[group][3], regExPhoneList[group][5]])
        if regExPhoneList[8] != '':
            phoneNumber += "x" + regExPhoneList[8]
        matches.append(phoneNumber)
    for group in range(len(regExEmailList)):
        matches.append(regExEmailList[group][0])
    return matches

def main():
    '''
    Defines the regex objects for phone numbers and email addresses.
    Copies modified text from searchResults() and pastes it back to the clipboard. 
    '''
    phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # Area Code
    (\s|-|\.)?              # Separator
    (\d\d\d)                # 3 digits
    (\s|-|\.)               # Separator
    (\d\d\d\d)              # Last 4 digits
    (x|ext\.)?              # Extension Separator
    (\d{2,5})?              # Extension Number
    )''', re.VERBOSE)

    email_addr_regex = re.compile(r'''(
    (\w[\w.]+)              # Account Name
    (@)                     # @ sign
    ([a-zA-Z0-9][\w.]+)     # domain after
    (\.[a-zA-Z]{2,4})       # TLD
    )''', re.VERBOSE)

    text = str(pyperclip.paste())
    searchResults = searchClipboard(phone_number_regex, email_addr_regex, text)
    
    if len(searchResults) > 0:
        pyperclip.copy('\n'.join(searchResults))
        print("Copied to clipboard:")
        print('\n'.join(searchResults))
    else:
        print(f'No phone numbers or email addresses found.')

###     RUN     ###
main()
###     STOP    ###