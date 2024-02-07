##  Python Code

##  This program will calculate the cost to clean a house based on the size and
##  type of cleaning

##  Developer: Shane Bottomley   Class: CMSC105   Date: 01/26/2024

def main():

    #welcome message and list cleaning types
    print("Thanks for choosing Shane's House Cleaning Services\n")
    print("We offer three types of cleanings:\n1. Full deep clean\n2. Regular clean\n3. Just vacuum and mop")
    print("\nThe cost of cleaning will depend on the size of your house. 1 bedroom is small, 2-3 is medium, and 4 or more is a large house")
    print("\nLet's get started on the cost to clean your home:")

    #define cleaning type and number of rooms variables from user input
    cleantype = eval(input("What type of cleaning would you like? Enter 1, 2, or 3: "))
    numrooms = int(input("How many rooms does your home have?: "))
    
    #define house size
    #small is 1 bedroom, medium is 2-3 bedrooms, large is 4 or more bedrooms
    if numrooms <= 1:
        size = "small"
    elif numrooms > 1 and numrooms <= 3:
        size = "medium"
    elif numrooms > 3:
        size = "large"

    #define basic cost of clean
    #Full deep clean is $150 + house size multiplier
    #Regular clean is $100 + house size
    #Vacuum and mop is $50 + house size
    if cleantype == 1:
        cost = 150
    elif cleantype == 2:
        cost = 100
    elif cleantype == 3:
        cost = 50
    else:
        print("You did not enter a valid cleaning type")

    #define house size multiplier
    #cost for small house is just the basic cost
    #cost for medium house is 2.5 * basic cost
    #cost for large house is 3.5 * basic cost
    if size == "small":
        multiplier = 1
    elif size == "medium":
        multiplier = float(2.5)
    elif size == "large":
        multiplier = float(3.5)

    #calculate and print total cost
    totalcost = str(round(cost * multiplier, 2))
    print("The total cost to clean your", size, "house is $" + totalcost)


#-------Execute-----------------
main()
