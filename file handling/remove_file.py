#Remove file permanently

import os
try:
    filename = input("Enter the file name: ")+'.txt'
    os.remove(filename)
    print(filename, "permanently deleted")
except:
    print("file does not exist")
