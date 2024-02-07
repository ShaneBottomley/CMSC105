##  Python Code

##  This is a calculator that asks the user for an operator and two numbers
##  

##  Developer: Shane Bottomley CMSC105   Date: 01/25/2024

def main():
    
    #Prompt user for input on operator 
    print("Would you like to add, subtract, multiply, or divide?")
    operator = str(input("Please enter +, -, *, or / : "))

    #Prompt user input on two numbers
    print("Now what two numbers are you working with? :")
    num1 = eval(input("Number 1: "))
    num2 = eval(input("Number 2: "))

    if operator == "+":
         print(num1 + num2)
    elif operator == "-":
         print (num1 - num2)
    elif operator == "*":
        print (num1 * num2)
    elif operator == "/":
        print (num1 / num2)
    else:
        print("You did not enter a valid operator")
        
        
    #---Execute-----------------------
main()
