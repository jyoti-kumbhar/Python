#Program to dynamically read the last line of the file.

file_name = "hello.txt"
try:
    with open(file_name,"r")as file:

        #read all lines from the file
        lines = file.readlines()
        
    if lines:
        #Extract and print the last line
        last_line = lines[-1].strip()
        print("Content of the last line : ",last_line)
    else:
        print(f"The file '{file_name}' is empty")
        
except Exception as e:
    print(f"Error reading file '{file_name}':{e}" )
    
