website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sifirdan Ileri Seviye Python Programlama"

print(len(kursAdi))
print(website[7:10])
print(website[22:])
print(kursAdi[:16])
print(kursAdi[-15:])
print(kursAdi[::-1])

s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

print('abc ' * 3)

name, surname, age, job = 'Sadik', 'Turan', 37, 'ogretmen'
x = 'Benim adim {0} {1} yasim {2} ve mesegim {3}.'.format(name, surname, age, job)

x = f"Benim adim {name} {surname} yasim {age} ve meslegim {job}."

print(x)