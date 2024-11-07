#Program to read a specific line from a file
line_number = 5
file = open("Students.txt")
currentline=1
for line in file:
       if (currentline ==line_number):
           print(line)
           break
       currentline=currentline+1

       
