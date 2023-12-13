#nested if
#income tax
print("nested if")
print()

print("Tax Calculation")
print()
age = int(input("Enter the age: "))
gender= input("Enter the Gender (Male / Female):")
income = float(input("Enter the annual income:"))

if (age >= 0 and age <18) or  (age > 60):
    print("No Tax TO Pay")
elif  age <60 :
    if gender == 'Male' or gender == 'male' or gender == 'MALE':
        taxper = 0.2
        print("Tax Amount Rs.",income * taxper)
    elif gender == 'Female' or gender == 'female' or gender == 'FEMALE':
            taxper = 0.1
            print("Tax Amount Rs.",income * taxper)
    else:
        print("Wrong Input! Gender can be Male/Female")
print()                
print("--"*20)
print("--"*20)


          

