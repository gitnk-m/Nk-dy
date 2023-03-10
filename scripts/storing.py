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
def store_form(name, email, one, two, three, four):
  sql_commmand='INSERT INTO formfilled (name, email, one, two, three, four) VALUES (%s, %s, %s, %s, %s, %s)'
  values=name, email, one, two, three, four
  mycursor.execute(sql_commmand,values)

  #commite to database
  mydb.commit()


#returning data to site
def get_data():
  mycursor.execute("SELECT * FROM formfilled")
  data=mycursor.fetchall()
  return data
    