##  Python Code

##  This program calculates how much milk a baby should eat
##  per feed based on weight and number of feeds according

##  Developer: Shane Bottomley CMSC105   Date: Jan 16, 2024


def main():
    #Defines the constant. Babies should intake 2.5oz a day for
    #every pound according to healthychildren.org
    intakeOz = float(2.5)

    #Prompts the user for their baby's weight
    babyWeight = (eval(input("Please enter your baby's weight in lbs: ") ))

    #Prompt user for feeds their baby eats per day
    feedsPerDay = (eval(input("Please enter the number of feeds per day: ") ))

    #Compute amount of oz baby should eat in a feed
    milkPerFeed = float((intakeOz * babyWeight) / (feedsPerDay))

    #Rounds milk per feed to a realistic number
    roundedMilkPerFeed = round(milkPerFeed, 2)
    
    #Display the rounded amount of oz baby should eat per feed
    print("Your baby should eat", roundedMilkPerFeed, "oz of milk per feed")
    
    #----Execute the main program ----------------------------
main()
