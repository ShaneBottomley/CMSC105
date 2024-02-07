##  Python Code

##  This program will calculate the cost to clean a house based on the size and
##  type of cleaning

##  Developer: Shane Bottomley   Class: CMSC105   Date: 01/26/2024


## -------- MAIN ---------------------------------------------
def main():

    #welcome message
    welcome_message()

    #get user input of number of rooms and clean type
    numrooms, cleantype = user_input()
    
    #define cleaning type and number of rooms variables from user input
    size_of_house = calculate_house_size(numrooms)
    cleaning_cost = calculate_cost_of_clean(cleantype)
    
    #calculate house size multiplier
    cost_multiplier = calculate_house_size_multiplier(size_of_house)
    
    #calculate and print total cost
    totalcost = str(round(cleaning_cost * cost_multiplier, 2))
    print("The total cost to clean your", size_of_house, "house is $" + totalcost)


## -------- Define Functions -------------------------

#define welcome message and list cleaning types
def welcome_message():
    print("Thanks for choosing Shane's House Cleaning Services\n")
    print("We offer three types of cleanings:\n1. Full deep clean\n2. Regular clean\n3. Just vacuum and mop")
    print("\nThe cost of cleaning will depend on the size of your house. 1 bedroom is small, 2-3 is medium, and 4 or more is a large house")
    print("\nLet's get started on the cost to clean your home:")

## ---------------------------------------------------
#user input function
def user_input():
    numrooms = int(input("How many rooms does your home have?: "))
    cleantype = int(input("What type of cleaning would you like? Enter 1, 2, or 3: "))
    return(numrooms, cleantype)

## ---------------------------------------------------
#define house size
#small is 1 bedroom, medium is 2-3 bedrooms, large is 4 or more bedrooms
def calculate_house_size(number_of_rooms):
    if number_of_rooms <= 1:
        size = "small"
    elif number_of_rooms > 1 and number_of_rooms <= 3:
        size = "medium"
    elif number_of_rooms > 3:
        size = "large"
    return(size)

## ---------------------------------------------------
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

#------- Execute ---------------------------------------
main()
