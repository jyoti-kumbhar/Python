#To check pH value
print("To check pH value")
print()
pH = float(input("Enter the pH value:"))
if pH < 7 and pH >= 0:
    print("pH is Acidic")    

if pH > 7 and pH <= 14:
    print("pH is Basic")

if pH == 7 :
    print("pH is Netural")
