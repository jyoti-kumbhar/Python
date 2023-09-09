#Arithematic Operators
print()
print("Arithematic Operators".center(40,"_"))
print()
x=float(input("Enter value of x:"))
y=float(input("enter the value of y:"))
print()
add=x+y
sub=x-y
multi=x*y
divi=x/y
mod=x%y
floordivi=x//y

print("Addition=",add)
print("Substraction=",sub)
print("Multiplication=",multi)
print("Division=",divi)
print("Modulus=",mod)
print("Floor Division=",floordivi)
print()

#Assignment Operators
print()
print("Assignment Operators".center(40,"_"))
print()
print("= Operator")
x = 5
print(x)
print()

print("+= Operator")
x = 5
x += 6
print(x)
print()

print("-= Operator")
x = 5
x -= 6
print(x)
print()

print("*= Operator")
x = 5
x *= 6
print(x)
print()

print("/= Operator")
x = 5
x /= 6
print(x)
print()

print("%= Operator")
x = 5
x %= 6
print(x)
print()

print("//= Operator")
x = 5
x //= 6
print(x)
print()

print("**= Operator")
x = 5
x **= 6
print(x)
print()

print("&= Operator")
x = 5
x &= 3
print(x)
print()

print("|= Operator")
x = 5
x |= 6
print(x)
print()

print("^= Operator")
x = 5
x ^= 6
print(x)
print()

print(">>= Operator")
x = 5
x >>= 6
print(x)
print()

print("<<= Operator")
x = 5
x <<= 6
print(x)
print()

#Comparison operators
print()
print("Comparison Operators".center(40,"_"))
print()
x=float(input("Enter value of x:"))
y=float(input("enter the value of y:"))
print()
print("Equal to equal to ")
print("x==y:",x==y)
print()
print("Not equal to ")
print("x!=y:",x!=y)
print()
print("Greater than ")
print("x>y:",x>y)
print()
print("Greater than or equal to")
print("x>=y:",x>=y)
print()
print("Lesser than ")
print("x<y:",x<y)
print()
print("Lesser than or equal to ")
print("x<=y:",x<=y)
print()
#Logical Operators
print()
print("Logical Operator".center(40,"_"))
print()
x=float(input("Enter value of x:"))
y=float(input("enter the value of y:"))
print()
print("And Operator")
print(x>y and x>=y)
print()
print("Or Operator")
print(x>y or x>=y)
print()
print("Not operator")
print(not(x))
print(not(y))
print()


#Identity operators
print()
print("Identity Operators".center(40,"_"))
print()
print("Is operator")
a=("Java","C","Python","SQL")
b=("Java","C","Python","SQL")
print(b is a)
print()
print("Is not operator")
print(b is not a)
print()


#Membership Operator
print()
print("Membership Operators".center(40,"_"))
print()
print("In operator")
print("Python" in a)
print()
print("Not in operator")
print("Python" not in b)
print()


#Bitwise operator
print()
print("Bitwise Operators".center(40,"_"))
print()
c=int(input("Enter the value of x:"))
d=int(input("Enter the value of y:"))
print("AND Operator")
print(c & d)
print()
print("OR Operator")
print(c | d)
print()
print("XOR Operator")
print(c ^ d)
print()
print("NOT Operator")
print(~c)
print(~d)
print()
print("LEFT SHIFT Operator")
print(c << d)
print()
print("RIGHT SHIFT Operator")
print(c >> d)
print()
