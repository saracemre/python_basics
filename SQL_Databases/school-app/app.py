from dbmanager import DbManager
import datetime
from Student import Student

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Student List\n2-Add Student\n3-Update Student\n4-Delete Student\n5-Add Teacher\n6-Lessons for Classes\n7-Exit(E)"
        while True:
            print(msg)
            operation = input("Choice: ")
            if operation == '1':
                self.displayStudents()
            elif operation == '2':
                self.addStudent()
            elif operation == '3':
                self.editStudent()
            elif operation == '4':
                pass
            elif operation == '5':
                self.db.addTeacher()
            elif operation == '6':
                pass
            elif operation == 'e' or operation == 'E':
                break
            else:
                print("Wrong Choice")

    def addStudent(self):
        self.displayClasses()
        classid = int(input("Which class: "))
        number = input("number: ")
        name = input("name: ")
        surname = input("surname: ")
        year = int(input("year: "))
        month = int(input("month: "))
        day = int(input("day: "))

        birthdate = datetime.date(year, month, day)
        gender = input("gender (E/K)")

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")


    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Which class: "))

        students = self.db.getStudentsByClassId(classid)

        print("Student List")
        for index, std in enumerate(students):
            print(f"{index + 1}-{std.name} {std.surname}")


app = App()
app.initApp()
