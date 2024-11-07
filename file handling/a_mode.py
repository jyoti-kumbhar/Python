#program to append file using 'a' mode

def append_file():
    file_Name = input("Enter the file name: ")
    file_Name = file_Name + '.txt'

#Open file for appending
    file1 = open(file_Name , 'a')
    data = input("Enter data to write in this file: ")
    data = data + '\n'
    file1.write(data)
    file1.close
    print("Write done on ", file_Name, "file")

append_file()
