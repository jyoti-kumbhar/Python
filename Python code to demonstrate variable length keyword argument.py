def func(**var):
    print("Last name:"+var["lname"])
    print("First name:"+var["fname"])
    for var in var.values():
        print(var,end=" ")
    for keys in var:
        print(keys)
    print(var)

Fname=input("Enter your first name:")
Lname=input("Enter your last name:")
func(fname="jyoti",lname="kumbhar")
