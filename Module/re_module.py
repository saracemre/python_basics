import re

result = dir(re)

# re module

string = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# re.findall()
# result = re.findall('Python', string)
# result = len(result)

# re.split()
# result = re.split(' ', string)
# result = re.split('R', string)

# re.sub()
# result = re.sub(' ', '-', string)
# result = re.sub('\s', '-', string) # \s = bosluk 

# re.search()
# result = re.search('Python', string)

# result = result.span() # Konum
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string



# regular expression

result = re.findall("[abc]", string) # Koseli parantez icindeki karakterleri arar.
result = re.findall('[a-e]', string) # a,b,c,d,e karakterlerini arar.
result = re.findall('[1-5]', string) # 1,2,3,4,5 karakterlerini arar.

result = re.findall('[^abc]', string) # abc disindaki karakterleri arar.
result = re.findall('[^0-9]', string) # Rakam olmayan karakterleri arar.

result = re.findall('...', string) # Her uclu grubu arar.(Nokta sayisina gore)
result = re.findall('Py..on', string)

result = re.findall('^a', string) # String belirtilen karakter ile basliyor mu sorusunu sorar.
result = re.findall('^P', string)

result = re.findall('a$', string) # String belirtilen karakter ile bitiyor mu sorusunu sorar.
result = re.findall('t$', string)
result = re.findall('saat$', string)

result = re.findall("sa*t", string) # a karakterinin sifir ya da daha fazla sayida olmasini kontrol eder.
result = re.findall("sa+t", string) # a karakterinin sifirdan fazla sayida olmasini kontrol eder.
result = re.findall("sa?t", string) # a karakterinin sifir ya da bir olmasini kontrol eder.

result = re.findall('a{2}', string)
result = re.findall('[0-9]{2}', string)

# | - alternatif seceneklerden birinin gerceklesmesi gerekir.

# () - gruplamak icin kullanilir.

# \ - Ozel karakterleri aramamizi saglar.
# \A - Belirtilen karakter string'in basinda mi?
result = re.findall('\APython', string)
# \Z - Belirtilen karakter string'in sonunda mi?
result = re.findall('saat\Z', string)
# \b - Belirtilen karakter kelimenin basinda ya da sonunda mi?
# \B - Belirtilen karakter kelimenin basinda ya da sonunda degil mi?

# \d - [0-9] ile ayni anlama gelir yani rakamlari arar.
# \D - [^0-9] ile ayni anlama gelir yani rakam olmayanlari arar.

# \s - Bosluk karakterleri arar.
# \S - Bosluk karakterleri disindakileri arar.

# \w - Alfabetik karakterler, rakamlar ve alt cizgi karakteri.
# \W - \w'nin tam tersi.



print(result)