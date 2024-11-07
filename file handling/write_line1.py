# open Internet file

import urllib.request
try:
   #url = "http://textfiles.com/adventure/aencounter.txt"
   url = input("Enter url:")
   file= urllib.request.urlopen(url)
   for line in file:
      decoded_line = line.decode("utf-8")
      print(decoded_line)
except:
      print("Can't open file")
