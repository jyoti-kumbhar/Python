# Program to create a file in 'x' mode

try:
    #specify the file name and open it in 'x' mode
    file_name = "name.txt"
    file = open(file_name, 'x')
    #write some content to the file
    file.write("This is a new file created in 'x' mode")
    print(f"file '{file_name}' Created successfully!")

except FileExistsError :
    print(f"Error: file'{file_name}'already exists use a different file name")
