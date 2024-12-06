import mysql.connector
import datetime
from connection import connection

class Student:

    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f"Added {Student.mycursor.rowcount} records.")
        except mysql.connector.Error as err:
            print(f"error: {err}")
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender) VALUES(%s,%s,%s,%s,%s)"
        values = (students)
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"Added {Student.mycursor.rowcount} records.")
        except mysql.connector.Error as err:
            print(f"error: {err}")
        finally:
            Student.connection.close()

    @staticmethod
    def updateStudentById(id, name, surname):
        sql = "UPDATE Student SET name = %s, surname = %s WHERE id = %s"
        values = (name, surname, id)
        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f"Added {Student.mycursor.rowcount} updates.")
        except mysql.connector.Error as err:
            print(f"error: {err}")
        finally:
            Student.connection.close()
    

# emre = Student(202, "Emre", "Sarac", datetime.datetime(2003, 4, 12), "E")
# emre.saveStudent()

students = [
    ("301", "Ahmet", "Yilmaz", datetime.datetime(2005, 5, 17), "E"),
    ("302", "Ali", "Can", datetime.datetime(2005, 6, 17), "E"),
    ("303", "Canan", "Tan", datetime.datetime(2005, 7, 7), "K"),
    ("304", "Ayse", "Taner", datetime.datetime(2005, 9, 23), "K"),
    ("305", "Bahadir", "Toksoz", datetime.datetime(2004, 7, 27), "E"),
    ("306", "Ali", "Cenk", datetime.datetime(2003, 8, 25), "E")
]

# Student.saveStudents(students)
    

connection = connection
mycursor = connection.cursor()

# A
# mycursor.execute("SELECT * FROM Student")
# result = mycursor.fetchall()
# print(result)

# B
# mycursor.execute("SELECT StudentNumber, Name, Surname FROM Student")
# result = mycursor.fetchall()
# print(result)

# C
# mycursor.execute("SELECT Name, Surname FROM Student WHERE Gender = 'K'")
# result = mycursor.fetchall()
# print(result)

# D
# mycursor.execute("SELECT * FROM Student WHERE DATE_FORMAT(Birthdate, '%Y') = 2003")
# result = mycursor.fetchall()
# print(result)

# E
# mycursor.execute("SELECT * FROM Student WHERE DATE_FORMAT(Birthdate, '%Y') = 2005 and Name = 'Ali'")
# result = mycursor.fetchall()
# print(result)

# F 
# mycursor.execute("SELECT * FROM Student WHERE Name LIKE '%an%' or Surname LIKE '%an%'")
# result = mycursor.fetchall()
# print(result)

# G
# mycursor.execute("SELECT COUNT(*) FROM Student WHERE Gender = 'E'")
# result = mycursor.fetchone()
# print(result)

# H
# mycursor.execute("SELECT * FROM Student WHERE Gender = 'K' ORDER BY Name")
# result = mycursor.fetchall()
# print(result)

Student.updateStudentById(20, "Mehmet", "Sayar")