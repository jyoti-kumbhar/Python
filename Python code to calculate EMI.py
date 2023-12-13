#program to calculate EMI Equated monthly

def EMI_calculation():
    name = input("Enter your name: ")
    principalAmt = int(input("Enter the Principal Amount:"))
    interest_rate = float(input("Enter the Rate of Interest:"))
    loan_term = int(input("Enter the Loan Term :"))

    #formula to calculate EMI
    interest_rate_1 = (interest_rate/100)/12
    loan_term = loan_term * 12
    EMI = (principalAmt * interest_rate_1 * (1 + interest_rate_1)**loan_term)/((1 + interest_rate_1)**loan_term - 1)

    print("Monthly EMI for  Car loan =",EMI)


EMI_calculation()
