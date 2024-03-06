##  Python Code

##  This program will prompt the user for how many people are going on a trip and how many days long it will be.
##  It will then ask the user for the cost of food and gas per each day of the trip.
##  Then it will display the total cost of food and gas, and how much it should cost total per person.
##  This program is based on USD currency

##  Developer: Shane Bottomley   Class: CMSC105   Date: 02/22/2024

##-----Functions------------------------------------

#Gets cost of food per day and adds to an array, returns the array of food cost per day
def get_food_cost_per_day(numberofdays):
    foodcostperday = list()
    count = 1
    while count <= numberofdays:
        foodcost = float(input(f'Please enter the cost of food on day number {count}: $'))
        foodcostperday.append(foodcost)
        count += 1
    return foodcostperday

#Gets cost of gas per day and adds to an array, returns the array of gas cost per day
def get_gas_cost_per_day(numberofdays):
    gascostperday = list()
    count = 1
    while count <= numberofdays:
        gascost = float(input(f'Please enter the cost of gas on day {count}: $'))
        gascostperday.append(gascost)
        count += 1
    return gascostperday

##------------Main--------------------------------------------

def main():
    #Welcome message
    print('Welcome to the Road Trip Calculator')
    print('Please follow the instructions to find out the total cost of food, total cost of gas,\n'
          'and how much each person should pay on your trip.\n')

    #Get user input for number of people on the trip and how many days long, convert to integer
    print('Please enter an integer for number of people and number of days')
    numofpeople = input('How many people are on the trip?: ')
    numofdays = input('How many days long is the trip?: ')
    numofpeople = int(numofpeople)
    numofdays = int(numofdays)

    #Get the gas cost per day using function, compute the total cost of gas
    print('\nEnter GAS cost per day:\n')
    costofgas = get_gas_cost_per_day(numofdays)
    totalcostofgas = sum(costofgas)
    totalcostofgas = round(totalcostofgas, 2)

    #Get the cost of food per day using function, compute total cost of food
    print('\nEnter FOOD cost per day\n')
    costoffood = get_food_cost_per_day(numofdays)
    totalcostoffood = sum(costoffood)
    totalcostoffood = round(totalcostoffood, 2)

    #Compute total cost and each persons share
    totalcost = round(totalcostofgas + totalcostoffood, 2)
    costperperson = round(totalcost / numofpeople, 2)

    #Print total cost of food, total cost of gas, total all together, and each persons cost
    print(f'\nThe total cost of food is ${totalcostoffood}')
    print(f'The total cost of gas is ${totalcostofgas}')
    print(f'The total cost of the trip is ${totalcost}')
    print(f'The cost for each person is ${costperperson}')

##---------Execute----------------------------------------------------
main()












