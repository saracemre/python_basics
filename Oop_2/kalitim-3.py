class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi olusturuldu.")
    
    def intro(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    def __init__(self, name, surname, age, number):
        Person.__init__(self, name, surname, age) # super().__init__(name, surname, age)
        self.number = number
        print("Student nesnesi olusturuldu.")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)

    def study(self):
        print(f'{self.number} numarali ogrenci ders calisiyor.')
    

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        Person.__init__(self, name, surname, age) # super().__init__(name, surname, age)
        self.branch = branch
        print("Teacher nesnesi olusturuldu.")

    def teach(self):
        print(f"{self.name} isimli ogretmen {self.branch} egitimi veriyor.")


p1 = Person('Ahmet','Turan', 20)
p1.intro() # person

s1 = Student('Emre', 'Sarac', 18, 101)
s1.intro() # student
s1.study()

t1 = Teacher('Sadik','Turan', 38, 'Matematik')
t1.intro()
t1.teach()
