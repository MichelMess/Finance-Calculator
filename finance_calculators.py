# This program creates a investment calculator and a home loan repayment calculator.  
import math
import sys 


# This bit of code requests the type of calculation the user wants to do.
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment \t - to calculate the amount of interest you'll earn on interest")
print("bond \t\t - to calculate the amount you'll have to pay on a home loan ")
calculator_type = input("Selection: ") 

# This bit of code performs a condition to find out the investment interest and/or interest.
if calculator_type == "investment" or calculator_type == "Investment" or calculator_type == "INVESTMENT":
    money_amount = float(input("Money deposit amount: "))
    interest_rate = float(input("The interest rate: "))
    yearsOfplan = float(input("How many years you intend to invest: "))        
    interest = input("simple interest or compound interest: ")

elif calculator_type == "Bond" or calculator_type == "bond" or calculator_type == "BOND":
    house_value = float(input("House value amount: "))
    bond_interest_rate = float(input("The interest rate: ")) 
    bond_yearsOfplan = float(input("How many months you intend to repay the bond: "))
    bond_repayment = (bond_interest_rate/12*house_value)/(1 - (1+bond_interest_rate/12)**(-bond_yearsOfplan))
    print("Total amount: ", bond_repayment)    
    sys.exit() 
    
else:
        print(sys.exit())

#All investment calculations below.   
# This bit of code performs a condition to find out the total amount of the selected interest. 
if interest == "simple interest": 
    total_simple_interest = money_amount*(1+(interest_rate/100)*yearsOfplan)
    print("Total amount: ", total_simple_interest)

elif interest == "compound interest":
    total_compound_interest = money_amount* math.pow((1+interest_rate/100),yearsOfplan)
    print("Total amount: ", total_compound_interest)
    
else:
        print("Interest type not selected.", sys.exit())
                
# Code ends here  
  
 
