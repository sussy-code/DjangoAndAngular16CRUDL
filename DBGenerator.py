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
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade INTEGER NOT NULL
    )
''')  # ID auto incremented

for _ in range(100):  # Adjust this number to create as many fake students as you need.
    cursor.execute('''
        INSERT INTO students_app_student (first_name, last_name, age, grade, adresse)
        VALUES (?, ?, ?, ?, ?)
    ''', (fake.first_name(), fake.last_name(), fake.random_int(min=18, max=25), fake.random_int(min=1, max=3), fake.adresse()))

connection.commit()
connection.close()