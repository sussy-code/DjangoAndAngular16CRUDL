from faker import Faker
from datetime import date
import sqlite3

fake = Faker()

fake.text()

class Student:
  
  classe = ""
  # birthdate = date()
  lastname = ""
  firstname = ""

connection = sqlite3.connect('studentsDB.sqlite3')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE students_app_student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        role TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade INTEGER NOT NULL,
        homeaddress TEXT NOT NULL
    )
''')  # ID auto incremented

import random
role = ('student', 'teacher', 'admin', 'parent')
for _ in range(100):  # Adjust this number to create as many fake students as you need.
  first_name = fake.first_name()
  last_name = fake.last_name()
  username = (first_name + last_name)[:7] + str(random.randint(10, 100))
  cursor.execute('''
      INSERT INTO students_app_student (username, first_name, last_name, role, age, grade, homeaddress)
      VALUES (?, ?, ?, ?, ?, ?, ?)
  ''', (username, first_name, last_name, random.choice(role), fake.random_int(min=18, max=25), fake.random_int(min=1, max=3), fake.address()))

# Adding real life example for cas testing purposes
cursor.execute('''
    INSERT INTO students_app_student (username, first_name, last_name, role, age, grade, homeaddress)
    VALUES ("yanregoj64", "yan", "regojo", "student", 21, 1, "1 rue de la paix")
  ''')

connection.commit()
connection.close()