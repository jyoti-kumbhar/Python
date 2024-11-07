# Create a file in Exclusive mode 'x'

try:
    with open("my file.txt",'x')as f:
        f.write("Hello, world !")
except FileExistsError:
    print("The file ' myfile.txt' already exists")
