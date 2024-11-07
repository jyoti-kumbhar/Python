#Program to create, read and write operation data on file

fileName =input("Enter file name: ")
fileName = fileName + ".txt"
print(fileName)
file1= open(fileName,'w')
file1.write("Hency,Rollno01\n")
file1.write("Manali,Rollno02\n")
file1.write("Diya,Rollno03\n")
file1.write("Shweta,Rollno04\n")
file1.write("Bhumi,Rollno05\n")
print("file created")
file1.close()
