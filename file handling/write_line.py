#program to write a line

#list of fruits
fruits = ["Apple\n" , "Orange\n" , "Grape\n" , "Watermelon\n"]
my_file = open('fruits.txt', 'w')
my_file.writelines(fruits)
my_file.close()
print("fruits.txt file created")

for i in range(2):
    data = input("Enter data = ")
    data = data + '\n'
    my_file = data
    
