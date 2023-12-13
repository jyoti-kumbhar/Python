#star triangle
num_row = int(input("Enter the size for pattern= "))
for row in range(num_row):
    for col in range(num_row-row-1):
        print(" ",end="")
    for col in range(row+1):
        print("*",end=" ")
    print()

