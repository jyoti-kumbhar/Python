#program to demonstrate call by refence

def change_me(list1):
    list1 = [20,24,32,35]
    print("Values inside the function: ", list1)

list1 = [101,201,301]
change_me(list1)
print("Values outside the function: ", list1)
   
