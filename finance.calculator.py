# This program allows the user to access two different financial calcualtors: an investment calcualtor and a home loan repayment calculator
import math

financial_calculator = input("investment - to calculate the amount of interest you'll earn on your investment \nbond       - to calculate the amount you'll have to pay on a home loan \n\nEnter either 'investment' or 'bond' from the menu above to proceed:            ").lower()

if len(financial_calculator) == 0:                                          # This part of the program will be invoked if the doesn't type anything 
    print("You have not entered anything, this program will not run!  ")

if financial_calculator == "investment":                                     # This part of the code prompts the user to enter the variables and calculates the return on their investment
    depositing_amount = float(input("Please enter the amount you are depositing: "))
    interest_rate = float(input("Please enter the interest rate as a number: "))
    how_many_years = float(input("Please enter how many years you are planning on investing: "))
    interest = (input("Please choose the type of interest you would like, choose from: 'simple' or 'compound' : "))

    if interest == "simple":
        interest_rate = interest_rate / 100
        total_amount = depositing_amount * math.pow((1+interest_rate), how_many_years)
        print(round(total_amount, 2))
        print(round(total_amount - depositing_amount, 2), f"is how much you gained after: {how_many_years:.2f} years" )
