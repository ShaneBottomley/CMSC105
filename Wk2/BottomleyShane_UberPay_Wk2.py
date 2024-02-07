##  Python Code

##  This program calculates the daily pay for an uber driver where they earn an hourly rate
##  of $14.50, plus 8% commison per mile, plus tips.

##  Developer: Shane Bottomley CMSC105   Date: Jan 17, 2024



def main():

    #welcome message
    print("Welcome to the Uber driver daily pay calculator\n")
    print("Let's get started calculating your daily pay!")
    
    #define the constant variables hourly rate (14.50) and commision rate (8% or .08)
    hrlyRate = float(14.50)
    commisionRate = float(.08)

    #prompt for user input
    milesDriven = eval(input("How many miles did you drive today?: ")) 
    hrsWorked = eval(input("How many hours did you work today?: "))
    tipsRec = eval(input("How much did you receieve in tips?: $"))

    #calculate the pay
    dailyWage = float(hrlyRate * hrsWorked)
    comPay = float(commisionRate * milesDriven)
    totalPay = float(dailyWage + comPay + tipsRec)

    #convert to strings to remove white space
    dailyWage = str(dailyWage)
    comPay = str(comPay)
    totalPay = str(totalPay)
    tipsRec = str(tipsRec)

    #cisplay Output
    print("\nYour daily wage is: $" + dailyWage)
    print("Your commision pay is: $" + comPay)
    print("You received: $" + tipsRec, "in tips")
    
    print("\nYour total pay for the day is: $" + totalPay)

    

    #------execute----------------------
main()
    

