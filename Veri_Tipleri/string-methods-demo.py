# msg = " Hello World "

# sonuc = msg.strip()

# print(sonuc)

sonuc = 'www.sadikturan.com'.strip('w.com')
print(sonuc)


website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sifirdan Ileri Seviye Python Programlama"

sonuc = kursAdi.lower()
sonuc = website.count('a')
sonuc = website.startswith('www')
sonuc = website.endswith('com')
sonuc = website.find('.com')
sonuc = website.find('com',0,10)
sonuc = kursAdi.find('Python')
sonuc = kursAdi.rfind('Python')
sonuc = kursAdi.index('Python')
sonuc = kursAdi.rindex('Python')

print(sonuc)
sonuc = kursAdi.isalpha()
sonuc = kursAdi.isdigit()
sonuc = 'Contents'.center(50,'*')
sonuc = 'Contents'.ljust(50,'*')
sonuc = 'Contents'.rjust(50,'*')

print(sonuc)
sonuc = kursAdi.replace(' ', '-')
sonuc = 'Hello World'.replace('World', 'There')
sonuc = kursAdi.split()

print(sonuc)