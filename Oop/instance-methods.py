import datetime
simdi = datetime.datetime.now()

class Person:

    # Yapici metotlar(constructor)
    def __init__(self, name, surname, year):

        #Object attributes
        self.name = name
        self.surname = surname
        self.year = year

    #Instance methods
    def intro(self):
        return f"Benim adim {self.name} ve soyadim {self.surname}"

    def calculate_age(self):
        return f"{simdi.year - self.year} yasindayim."



p1 = Person("Emre", "Sarac", 2003)
p2 = Person("Mustafa", "Sarac", 1970)

print(p1.intro())
print(p1.calculate_age())
print(p2.intro())
print(p2.calculate_age())
