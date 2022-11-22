#import the SQLite3 module
import sqlite3
import pandas as pd

#Create connection to database
conn = sqlite3.connect("first.db")

#Create cursor object
cursor = conn.cursor()

#Create students table
cursor.execute('''CREATE TABLE students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    major_code INTEGER,
                    grad_date datetime,
                    grade REAL NOT NULL)''')

#Add a row of data to students table
cursor.execute('''INSERT INTO students VALUES (101, 'ALex', 'alex@codeeu.com', 32, '2022-05-16', 'Pass')''')

#Insert multiple values into table at once
students = [(102, 'Joe', 'joseph@codeu.com', 32, '2022-05-16', 'Pass'),
            (103, 'Stacy', 'stacy@codeu.com', 10, '2022-05-16', 'Pass'),
            (104, 'Angela', 'angela@codeu.com', 21, '2022-12-20', 'Pass'),
            (105, 'Mark', 'mark@codeu.com', 21, '2022-12-20', 'Fail'),
            (106, 'Nathan', 'nathaniel@codeu.com', 21, '2022-12-20', 'Pass')
            ]
 
# Insert values into the students table
cursor.executemany('''INSERT INTO students VALUES (?,?,?,?,?,?)''', students)

#Iterate through all rows in students table
for row in cursor.execute("SELECT * FROM students"):
    print(row)

#fetchone() example
#Return first row in students
callone = cursor.execute("SELECT * FROM students").fetchone()
print(callone)

#fetchmany() example
#Return first however many rows based on the argument passed in the function
call_two = cursor.execute("SELECT * FROM students").fetchmany(4)
print(call_two)

#fetchall() example
#return all rows in students
call_three = cursor.execute("SELECT * FROM students").fetchall()
print(call_three)

# Return the number of rows with a passing grade, print only one row/value set
call_four = cursor.execute("""SELECT COUNT(*) FROM students WHERE Grade = 'Pass';""").fetchone()
print(call_four)

#SQLite with Panda Dataframes
#read_sql_query() -> takes in a query and a connection as parameters and returns a DataFrame

# Create a new dataframe from the result set
df = pd.read_sql_query('''SELECT * from students;''', conn)
 
# Show new dataframe
print(df)
