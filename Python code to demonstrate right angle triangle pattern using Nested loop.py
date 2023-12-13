#star rightangle triangle
limit = int(input("Enter the size for pattern= "))
for row in range (limit +1):
    for col in range(1, row + 1):
        print("*",end=" ")
    print()



#number rightangle triangle   
limit = int(input("Enter the size for pattern= "))
for row in range (limit +1):
    for col in range(1,row+1 ):
        print(row,end=" ")
    print()
