import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "SELECT * FROM Student WHERE id = %s"
        value = (id, )
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def getClasses(self):
        sql = "SELECT * FROM Class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def getStudentsByClassId(self, classid):
        sql = "SELECT * FROM Student WHERE classid = %s"
        value = (classid, )
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"Added {self.cursor.rowcount} records.")
        except mysql.connector.Error as err:
            print(f"error: {err}")

    def editStudent(self, student: Student):
        sql = "UPDATE Student SET StudentNumber = %s, Name = %s, Surname = %s, Birthdate = %s, Gender = %s, ClassId = %s WHERE id = %s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"Added {self.cursor.rowcount} updates.")
        except mysql.connector.Error as err:
            print(f"error: {err}")

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db has been deleted")

db = DbManager()

# student = db.getStudentById(5)[0]

# print(student.name)

# students = db.getStudentsByClassId(1)
# for i in students:
#     print(i.name)


