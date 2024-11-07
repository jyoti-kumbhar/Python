import sqlite3

conn=sqlite3.connect('demo.db')
cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS fruits")
cursor.execute('''CREATE TABLE fruits(
               NAME TEXT,
               QUANTITY_AVA INTEGER,
               PRICE_KG REAL);
 ''')

cursor.execute('''INSERT INTO fruits VALUES('Kiwi', 20, 30.2)''')
cursor.execute('''INSERT INTO fruits VALUES('Watermelon', 10, 20.3) ''')
cursor.execute('''INSERT INTO fruits VALUES('Mango', 50, 40.6) ''')
cursor.execute('''INSERT INTO fruits VALUES('Apple', 15, 45.4) ''')

#select the data
data=cursor.execute('''SELECT * FROM fruits;''')
for i in data :
    print(i)    
print("------")

#select particular data
data=cursor.execute("SELECT NAME, PRICE_KG from fruits;")
for i in data:
    print(i)
print("------")

#delect particular data
cursor.execute("DELETE FROM fruits WHERE NAME = 'Kiwi';")

#select the data by order
data=cursor.execute("SELECT * FROM fruits ORDER BY NAME;")
for i in data:
    print(i)
print("------")

#update an data
cursor.execute("UPDATE fruits SET PRICE_KG = 56 WHERE NAME='Apple';")

data=cursor.execute("SELECT * FROM fruits ORDER BY NAME;")
for i in data:
    print(i)
print("------")

#put some limits
data=cursor.execute("SELECT * FROM fruits ORDER BY NAME DESC LIMIT 2 ")
for i in data:
    print(i)
print("------")


cursor.close()
conn.close()