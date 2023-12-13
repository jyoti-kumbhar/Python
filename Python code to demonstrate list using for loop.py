#Name : Jyoti kumbhar   Rollno. 89

print("for over list".center(40,"_"))
print()
val = [2,'two',3,4.4,'A' ]
for i in val:
    print(i)
print()
print("_"*40)




print()
print("for over Dictionary".center(40,"_"))
print()

student_D = {'meena' : '40','jiya' : '50','priya' : '22','sarika' : '45'}

print("Keys:")
for keys in student_D:
    print(keys,end=' ')
print()

print()
print("Values:")
for values in student_D.values():
    print(values,end=' ')
print()

print()
print("Items:")
for items in student_D.items():
    print(items,end=' ')
print()

print()
print("Keys and Values:")
for k in student_D:
    print(k,student_D[k])
print("_"*40)




print()
print("Tuple".center(40,"_"))
print()

num = (10,20,30,40)
s = 0
for t in num:
    s = s + t
print("Sum :" ,s)
print()
print("_"*40)





print()
print("for over string".center(40,"_"))
print()

word = input("Enter word/sentence :")
for c in word:
    print(c.upper(),end=' ')
print()
print("_"*40)
