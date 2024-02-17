##  Password Checker

##  This program checks that the password is between 8-15 characters, contains at least one
##  digit, at least one alphabetic character, and no spaces. It will reprompt for the password
##  if any of the password conditions aren't met.

##  Developer: Shane Bottomley   Class: CMSC105   Date: 02/17/2024

##------Functions---------------------------------

##Function 1
#check length of password between min and max
def check_length(password, min, max):
    passlength = len(password)
    if passlength < min:
        print('Your password is too short')
    elif passlength > max:
        print('Your password is too long')
    else:
        return True

##Function 2
#check password for num of digits and num of alpha characters needed
def check_chardigits(password, digitsneeded, alphasneeded):
    #initialize variables for number of digits and number of alphas
    numofdigits = 0
    numofalpha = 0
    #loop through password and count number of digits and alphas
    for index in password:
        if index.isdigit():
            numofdigits +=1
        elif index.isalpha():
            numofalpha +=1
    #check number of digits and number of alphas is
    if numofdigits < digitsneeded:
        print(f'Your password must contain at least {digitsneeded} digit(s)')
    elif numofalpha < alphasneeded:
        print(f'Your password must contain at least {alphasneeded} alphabetic character(s)')
    else:
        return True

##Function 3
#check for too many spaces in password
def too_many_spaces(password, spacesallowed):
    numofspaces = 0
    for index in password:
        if index == ' ':
            numofspaces += 1
    if numofspaces > spacesallowed:
        print('Your password has too many spaces')
    else:
        return False

##--------Main-------------------------------------------------------------------
def main():
    while True:
        #get user input for password
        userpass = input('Please enter a password: ')

        #check for password length between 8-15 characters
        if check_length(userpass, 8, 15) == True:
            pass
        else:
            continue

        #check for 1 digit and 1 alphabetic character
        if check_chardigits(userpass, 1, 1) == True:
            pass
        else:
            continue

        #check for spaces in password
        if too_many_spaces(userpass, 0) == False:
            pass
        else:
            continue

        #tell user password is valid
        print('Your password is valid and has been accepted!')
        break
##-------Execute---------------------------------
main()
