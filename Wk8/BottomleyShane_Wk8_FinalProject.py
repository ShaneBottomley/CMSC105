##  Python Code

##  Welcome to Shane's Services. This program prompts the user to choose a service
##  and will list a price for that service after it gathers some information.
##  Shane's Services also offers a senior discount, users will be prompted to enter
##  their age, anyone ages 55 and older gets a 10% senior discount.

##  Developer: Shane Bottomley   Class: CMSC105   Date: 02/27/2024

##--------Functions--------------------------------------------

#ask user to choose service, return choice
def choose_service():
    print("Welcome to Shane's Services\n")
    print('We offer two services:\n1. House Cleaning\n2. Yard Service')
    print('\nWhich service interests you today?')
    while True:
        ## Check for integer
        try:
            choice = int(input('Enter 1 or 2: '))
        except ValueError:
            print('Please enter a valid service')
            continue

        ## Check for valid service, able to easily scale services
        if 0 < choice < 3:
            return choice
            break
        else:
            print('Please enter a valid service')
            continue

#determine senior discount eligibility, return discount multiplier
#able to scale for more discounts, i.e. super senior, children discount, member discount, etc
def determine_discount():
    print('We also offer a 10% senior discount, how old are you?:')
    while True:
        try:
            age = int(input('Age: '))
            break
        except ValueError:
            print('Please enter an integer for your age')
            continue
    if age >= 55:
        discountmultiplier = float(0.10)
    else:
        discountmultiplier = 0
    return discountmultiplier

##------Cleaning Service functions-----
#define welcome message and list cleaning types
def clean_welcome_message():
    print("Thanks for choosing Shane's House Cleaning Services\n")
    print("We offer three types of cleanings:\n1. Full deep clean\n2. Regular clean\n3. Just vacuum and mop")
    print("\nThe cost of cleaning will depend on the size of your house.\n1 bedroom is small, 2-3 is medium, and 4 or more is a large house")
    print("\nLet's get started on the cost to clean your home:")

#cleaning user input
def clean_user_input():
    while True:
        try:
            numrooms = int(input("How many rooms does your home have?: "))
            cleantype = int(input("What type of cleaning would you like? Enter 1, 2, or 3: "))
        except ValueError:
            print('Please enter integers for number of rooms and cleaning type')
            continue
        if 0 < cleantype <= 3:
            return(numrooms, cleantype)
        else:
            print('Please enter a valid cleaning type')
            continue

#get house size
#small is 1 bedroom, medium is 2-3 bedrooms, large is 4 or more bedrooms
def calculate_house_size(number_of_rooms):
    if number_of_rooms <= 1:
        size = "small"
    elif number_of_rooms > 1 and number_of_rooms <= 3:
        size = "medium"
    elif number_of_rooms > 3:
        size = "large"
    return(size)

#define basic cost of clean
#Full deep clean is $150 + house size multiplier
#Regular clean is $100 + house size
#Vacuum and mop is $50 + house size
def calculate_cost_of_clean(type_of_clean):
    cost = 0
    if type_of_clean == 1:
        cost = 150
    elif type_of_clean == 2:
        cost = 100
    elif type_of_clean == 3:
        cost = 50
    else:
        print("You did not enter a valid cleaning type")
    return(cost)

#define house size multiplier
#cost for small house is just the basic cost
#cost for medium house is 2.5 * basic cost
#cost for large house is 3.5 * basic cost
def calculate_house_size_multiplier(size_of_house):
    if size_of_house == "small":
        multiplier = 1
    elif size_of_house == "medium":
        multiplier = float(2.5)
    elif size_of_house == "large":
        multiplier = float(3.5)
    return(multiplier)

def cleaning_service_main():
    # welcome message
    clean_welcome_message()

    # get user input of number of rooms and clean type
    numrooms, cleantype = clean_user_input()

    # define cleaning type and number of rooms variables from user input
    size_of_house = calculate_house_size(numrooms)
    cleaning_cost = calculate_cost_of_clean(cleantype)

    # calculate house size multiplier
    cost_multiplier = calculate_house_size_multiplier(size_of_house)

    # calculate and print total cost
    cleantotalcost = float(round(cleaning_cost * cost_multiplier, 2))
    return cleantotalcost

##---Yard Service Functions--------
#welcome user to yard cleaning services
def yard_welcome_message():
    print('Welcome to the Yard Service')
    print('We provide 3 services: Mowing, Edging, and Shrub Pruning')
    print('The cost of this service will depend on your yard size and how many shrubs you have')
    print("Please provide the following information to determine the cost: ")

#get user input for yard width, yard length, and number of bushes, calculate sq footage of yard
def yard_user_input():
    while True:
        try:
            yardwidth = int(input('Please enter the width of your yard rounded to the nearest foot: '))
            yardlength = int(input('Please enter the length of your yard rounded to the nearest foot: '))
            numofshrubs = int(input('Please enter the amount of shrubs in your yard: '))
            break
        except ValueError:
            print('Please enter integers only\n')
            continue
    yardsquarefootage = yardwidth * yardlength
    return(yardwidth, yardlength, numofshrubs, yardsquarefootage)

#calculate cost of mowing, $0.012 per sq foot of yard
def cost_of_mowing(yardsquarefootage):
    costofmow = 0.012 * yardsquarefootage
    return costofmow

#calculate cost of edging, $0.20 per linear foot of yard
def cost_of_edging(yardlength, yardwidth):
    linearfootage = (yardwidth * 2) + (yardlength * 2)
    costofedge = linearfootage * 0.20
    return costofedge

#calculate cost of pruning bushes, $4 per bush
def cost_of_prune(numofbushes):
    costofprune = numofbushes * 4.00
    return costofprune

#get user input, calculate total costs of yard services
def yard_service_main():
    #get user input
    myyardwidth, myyardlength, mynumofbushes, mysqft = yard_user_input()

    #calculate cost of mowing, edging, and pruning
    mymowcost = cost_of_mowing(mysqft)
    myedgecost = cost_of_edging(myyardlength, myyardwidth)
    myprunecost = cost_of_prune(mynumofbushes)

    #add total cost of services
    totalcostofyardservice = mymowcost + myedgecost + myprunecost
    return(totalcostofyardservice)

##---------MAIN--------------------------------------------------------------------------------------
def main():
    #assign variables
    totalcostbeforediscount = float(0)
    mydiscount = float(0)
    totalcostafterdiscount = float(0)

    #choose a service, 1 for cleaning and 2 for yard service
    userchoice = choose_service()
    if userchoice == 1:
        totalcostbeforediscount = cleaning_service_main()
    elif userchoice == 2:
        totalcostbeforediscount = yard_service_main()
    else:
        pass

    ##determine senior discount eligibility and %
    mydiscountmultiplier = determine_discount()

    #calculate discount and subtract from total cost
    mydiscount = round(mydiscountmultiplier * totalcostbeforediscount, 2)
    totalcostafterdiscount = totalcostbeforediscount - mydiscount

    #print total cost of service
    print(f'The discount is ${mydiscount}')
    print(f'\nThe total cost for the service is ${totalcostafterdiscount}')
##-------Execute Main Program---------------------------------------------------------------
main()