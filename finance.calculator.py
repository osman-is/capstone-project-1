# This program allows the user to access two different financial calcualtors: an investment calcualtor and a home loan repayment calculator
import math

financial_calculator = input("""\n1. investment - to calculate the amount of interest you'll earn on your investment 
2. bond       - to calculate the amount you'll have to pay on a home loan 
\nEnter either 'investment' or 'bond' from the menu above to proceed:  """).lower()

if financial_calculator == "investment":                                     # This part of the code prompts the user to enter the variables and calculates the return on their investment
    depositing_amount = float(input("Please enter the amount you are depositing: ")) # how much they are depositing 
    interest_rate = float(input("Please enter the interest rate as a number: ")) # interest rate
    how_many_years = int(input("Please enter how many years you are planning on investing: ")) # how long they want to save for
    interest = (input("Please choose the type of interest you would like, choose from: 'simple' or 'compound' : ")) # type of interest 'simple' or 'compound'

# Depending on whether or not they typed “simple” or “compound” , the appropriate amount will be calculated and the amount they will get back after the given period will be printed.

    if interest == "simple":
        interest_rate = interest_rate / 100
        total_amount = depositing_amount *(1+interest_rate * how_many_years) # This is the formula the program uses to calculate total amount.
        print(f"The total amount you'll get is: R{total_amount:.2f} ")
        print(f" The total gain is: R{total_amount - depositing_amount:.2f}), after: {how_many_years} years")
    
    elif interest == "compound":
        interest_rate = interest_rate / 100
        total_amount = depositing_amount * math.pow((1+interest_rate), how_many_years) # # again this formula is used to calculate total amount.
        print(round(total_amount, 2))
        print(f" The total gain is: R{total_amount - depositing_amount:.2f}, after: {how_many_years} years" )
    
    # If the user enters bond, the amount that a person will have to be repaid on a home loan each month is calculated on the below code.

elif financial_calculator == "bond":                  # if the user enters bond they will be asked to input the following:
    present_house_value = float(input("Please enter the current house value: ")) # current house value
    interest_rate = float(input("Please enter the interest rate as a number: ")) # interest rate
    number_of_months = float(input("Please enter the number of months you plan to repay the bond: "))  # and the number of months they want to repay the loan


    interest_rate = interest_rate / 100
    interest_rate = interest_rate / 12
    repayment = (interest_rate * present_house_value) / (1 - (1 + interest_rate) ** (- number_of_months)) # This is the formula the program uses to calculate repayment amount.
    print(f"The total repayment per month is: R{repayment:.2f}")


else:
    len(financial_calculator) == 0                                          # This part of the program will be invoked if the user doesn't type anything 
    print("You have not entered anything, this program will not run!  ")

