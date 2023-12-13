
#Name: Jyoti Kumbhar      Rollno. 89

#program to calculate simple interest

def calculate_SI():
    name=input("Enter your name:")

    #input principal amount
    principalAmt = int(input("Enter Principal Amount:"))
    interest_rate = int(input("Enter Rate of Interest:"))
    num_months = int(input("Enter Numbers of years:"))

    #formula to calculate simple interest
    simple_interest = (principalAmt * interest_rate * num_months)/100

    print("Simple Interset =",simple_interest)


calculate_SI()
