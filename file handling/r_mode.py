#Program to read file using 'r' mode

fileName =input("Enter file name: ")
fileName = fileName + ".txt"

try:
  file1=open (fileName,'r')
  for lines in file1:
      print(lines)
  file1.close()
except:
      print(fileName," file does not exist")
