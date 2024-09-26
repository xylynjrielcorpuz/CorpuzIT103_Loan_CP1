'''
Problem analysis:
    1. Ask the user for their monthly salary to chech the eligibility. 
    2. The eligible monthly salary to approve the bank loan is 30,000 PHP. Therefore if the monthly salary of the user is 
        less than 30,000, the loan request will not proceed. Otherwise, proceed to number 3.
    3. Ask the user the amount that they request to loan. It must be less than ten times their salary. Thus, if it exceed,
        the loan request will not proceed. Otherwise, proceed to number 4.
    4. Ask the user for how many months they will pay the loan amount that they requested.
    5. Add ten percent interest to the loan amount they requested.
    6. Divide the loan amount with interest to the duration the user wants to pay.
    7. The Loan is approved. Display the loan amount with interest and the monthly amount payable that the user will pay. 
'''

print("Good day! Please answer a few questions to approve your loan request. ")

#Ask salary  (1)
MonthlySalary = float(input("How much is your monthly salary? (Do not use comma): "))

#Eligibility_Monthly Salary (2)
if MonthlySalary < 30000.00:
    print("Sorry your bank loan request is not approved due to your insufficient income. Thank you!.")

else:
#Eligibility_Loan Amount (3)
    LoanAmount = float(input("Please enter the amount that you request to loan. (Do not use comma): "))
    if LoanAmount <= 10*MonthlySalary:
  #Duration of payment, Interest, and Amount payable (4, 5, 6)
        Duration = int(input("How many months would you like to pay the loan you've requested?: "))
        Interest = LoanAmount*0.10
        NewLoanAmount = Interest + LoanAmount
        Payment = NewLoanAmount/Duration
  #Loan is approved (7)
        print(f"Congratulations! Your loan request of {LoanAmount:.2f} PHP is approved! The amount of your payable loan is {NewLoanAmount:.2f} PHP.")
        print(f"You will pay {Payment:.2f} PHP for {Duration} months")
        print("Thank you!")

    else:
        print("Sorry your bank loan is not approved. The amount that you are requesting is too high. Thank you!")


        
        



