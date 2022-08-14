# This Program assists custumers assist in making good financial choice
#This done by providing service of different calculators from them to choose from.
#Choice of calculator will depend on their goals
import math

print ("Welcome to Financial Solutions. We provide services to help YOU make smart financial decisions.\n")

print (" To continue choose either Investment or Bond from the menu :\n" )

print ("Investment            - to calculate the amount of interest that will be earned")
print ("Bond                  - to calculate the amount that will be paid on home loan\n")

#step 1 get user input
user_choice = input("Enter your choice :\n")

#step 2 check if input is correct
#can only compare things if they are the same
#to take any spelling of same word just make answer all answers uppercase and compare that to uppercase INVESTMENT/BOND.
#if,elif,else used to test 3 conditions. 1.if investment. 2.if bond. 3.if any other word
user_choice = user_choice.upper()


if user_choice == "INVESTMENT" :
    deposit_amt = int(input("How much are you depositing:""\n"))
    interest_amt = int(input("At what yearly interest rate :""\n"))
    years_amt = int(input("How many years will you be investing:""\n"))

    user_typeint = input ("Do you want Compound or Simple interest: ""\n")
    user_typeint = user_typeint.upper()

#use if to test 2 coditions of compound or simple

    if user_typeint == "COMPOUND":
        compound_calcint = deposit_amt * math.pow((1+interest_amt/100), years_amt)
        user_interest = compound_calcint
        print(f"Your earned interest will be {user_interest}")

    if user_typeint == "SIMPLE":
        compound_calcint = deposit_amt * (1+(interest_amt/100) * years_amt)
        user_interest = compound_calcint
        print(f"Your earned interest will be {user_interest}")


elif user_choice == "BOND" :
    present_amt = int(input("What is the present value of the house:""\n"))
    interest_amt = int(input("At what monthly interest rate :""\n"))
    months_amt = int(input("How many months will you be repaying :""\n"))
    bond_amt = (interest_amt* present_amt)/(1 - (1 + interest_amt ))**-(months_amt)  
    print(f"You need to repay {bond_amt}")
else :
    print ("Try Again can only choose between Investment or Bond.")
