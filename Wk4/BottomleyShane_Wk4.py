## Python Code

## This program calculates the speed(MPH) of an object when given the distance(MILES)
## and time(MINUTES)

## Shane Bottomley CMSC105 01/29/2024

    #define welcome message function
def welcome():
    print("Welcome to the speed calculator!")
    
    #define function to compute speed given distance & time
def calculate_speed(distance1, time1):
    speed1 = distance1 / time1
    return(speed1)

def main():
    #welcome message
    welcome()
    
    #get user input for distance and time
    distance = float(input("Please enter the distance in miles: "))
    time = float(input("Please enter the time in minutes: "))

    #change minutes to float hours
    time = time / 60
    
    #call function to calculate speed
    speed = str(round(calculate_speed(distance, time), 2))

    #output speed
    print("\nThe speed is", speed, "MPH")

    ##--------EXECUTE--------------------------------
    
main()
