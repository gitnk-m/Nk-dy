import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Qwerty!6789",
  database="mydatabase"
)

mycursor = mydb.cursor()

#To create the database (use only once)
#mycursor.execute("CREATE DATABASE mydatabase")

#To view the database
'''mycursor.execute("SHOW DATABASES")
for db in mycursor:
  print(db)'''

# To create table (use only once)
'''mycursor.execute("CREATE TABLE formfilled (user_id INT AUTO_INCREMENT PRIMARY KEY, \
                  name VARCHAR(100), \
                  email VARCHAR(200), \
                  one VARCHAR(10), \
                  two VARCHAR(10), \
                  three VARCHAR(10), \
                  four VARCHAR(10))")'''

#show table
'''mycursor.execute("SELECT * FROM formfilled")
for i in mycursor.description:
  print(i)'''


#adding data to database
'''sql_commmand='INSERT INTO formfilled (name, email, one, two, three, four) VALUES (%s, %s, %s, %s, %s, %s)'
values=name, email, one, two, three, four
mycursor.execute(sql_commmand,values)

#commite to database
mydb.commit()'''


#view data in table
'''mycursor.execute("SELECT * FROM formfilled")
data=mycursor.fetchall()
for i in data:
  print(i)'''
  



"""
    ::color ::
https://colorhunt.co/palette/6096b493bfcfbdcdd6eee9da
https://colorhunt.co/palette/edf1d69dc08b60996640513b
https://colorhunt.co/palette/182747562b08647e68d8d8d8
https://colorhunt.co/palette/eeeeeedededeff4949c10000
https://colorhunt.co/palette/e7e6e1f7f6e7f2a154314e52
https://colorhunt.co/palette/f7f1e5e7b10a8981214c4b16

"""