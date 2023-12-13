#Program to demonstrate zip and unzip
name = [ "priya" , "gauri" , "yogita" , "swara" ]
rollno = [ 12 , 18 , 23 , 28 ]
mobile_no = [1232, 4563, 1312, 4654 ]

#using zip()
mapped = zip( name, rollno, mobile_no)
print(set(mapped))

#using unzip()
zipval = {("priya" , 12 , 1232)}
print(zipval)
name, rollno, mobile_no = zip(*zipval)
print(name)
print(rollno)
print(mobile_no)
