##  Python Code

##  This program gets a line from the user, it strips the line and then counts spaces in the line.
#   It assumes one space as two words. If the line is not between 7-11 words,
#   it mocks user by repeating back a "mock line" and the first 15 indexes, cutting them off and then
#   it asks for a new line.

#   If line is between 7-11 words, it checks for initials 'sb'. If sb is not in line, it asks again
#   Once line is between 7-11 words with one word being initials 'sb' it ends.

#   If line is exactly 8 words it gets a BING BING BING for the perfect amount of words.


##  Developer: Shane Bottomley   Class: CMSC105   Date: 02/15/2024

##----------Function----------------

#check initials in line, return True or False
def check_initials(linelowercase, initials):
    if initials in linelowercase:
        print('\nAnd thanks for adding my initials "sb" in your line!\n\nThe End!')
        return(True)
    else:
        print(f"\nBut why didn't you add my initials 'sb' in your line?\n\n")
        return(False)

#make a mockline by upper casing even indexes and lowercasing all others
def mockline(lineofwords):
    newline = ' '
    index = 0
    for char in lineofwords:
        if index % 2 == 0:
            char = char.upper()
        else:
            char = char.lower()
        index = index + 1
        newline = newline + char
    return(newline)

    
##---------------Main----------------------

def main():
    while True:
        #get user input and assing to line variable
        line = input('Please enter a line of words: ')

        #strip line and get number of spaces in line and assign to spacescount
        spacescount = 0
        line = line.strip()
        spacescount = line.count(' ')

        #lowercase line to check for initials in line
        linelowercase = line.lower()
        initialcheck = None

        #create a mock line. upper and lower every other index, use only first 15 indexes
        mymockline = mockline(line)
        mymockline = mymockline[:15]

        #if user enters less than "7 words" aka 6 spaces, print not enough words
        if spacescount < 6:
            print('\n"' + mymockline + '"' + ' -STOP! You did NOT enter enough words!')
            print('\n\nYou entered', spacescount + 1, 'words. Try putting more words.\n\n')
            continue
            
        #greater than "11 words"/10 spaces, print too many words
        elif spacescount > 10:
            print('\n"' + mymockline + '"' + ' -NOPE! You entered WAYYY too many words!!!')
            print('\n\nYou entered', spacescount + 1, 'words. Try putting less words.\n\n')
            continue

        #easter egg of "8 words"/7 spaces gets the bingo jackpot
        elif spacescount == 7:
            print('\n\nBING!!\nBING!!\nBING!!\nThe exact perfect-o amount of words!')

            #check for initials if line is a good number of words
            initialcheck = check_initials(linelowercase, 'sb')
            if initialcheck == True:
                break
            else:
                continue
            
        #between 7 to 11 words/6 to 10 spaces but not 8 words is a good amount, but not perfect
        else:
            print('\nNice! That was a good amount of words (:')

            #check for initials if line is a good number of words
            initialcheck = check_initials(linelowercase, 'sb')
            if initialcheck == True:
                break
            else:
                continue
##---------Main End---------------
        
main()
