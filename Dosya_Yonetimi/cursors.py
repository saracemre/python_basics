# f.seek(a) a. stringe goturur.
# f.readline() bir satir okur.
# f.readlines() butun satirlari liste halinde verir;
# f.close() dosyayi kapatir.
# f.closed dosyanin kapali olup olmadigini sorar.

f = open('msg.txt')

print(f.read())
print(f.read())

f.seek(0)
print(f.readable())

# >>> f.seek(0)
# >>> f.read()
# 'hello world.\nMerhaba Dunya'
# >>> f.read()
# '\nemre\nasdf\n'
# >>> f.read()
# ''
# >>> f.seek(5)
# >>> f.read()
# ' world.\nMerhaba Dunya\nemre\nasdf\n'
# >>> f.seek(0)
# >>> f.readline()
# 'birinci satir.\n'
# >>> f.readline()
# 'ikinci satir.\n'
# >>> f.readline()
# 'ucuncu satir.\n'
# >>> f.readline()
# 'dorduncu satir.\n'
# >>> f.readline()
# 'besinci satir.\n'
# >>> f.readline()
# '\n'
# >>> f.readline()
# ''
# >>> f.seek(0)
# >>> f.readlines()
# ['birinci satir.\n', 'ikinci satir.\n', 'ucuncu satir.\n', 'dorduncu satir.\n', 'besinci satir.\n', '\n']
# >>> satirlar = f.readline()
# >>> satirlar
# ''
# >>> f.seek(0)
# >>> satirlar
# ''
# >>> f.seek(0)
# >>> satirlar = f.readlines()
# >>> satirlar
# ['birinci satir.\n', 'ikinci satir.\n', 'ucuncu satir.\n', 'dorduncu satir.\n', 'besinci satir.\n', '\n']
# >>> satirlar[0]
# 'birinci satir.\n'
# >>> satirlar[3]
# 'dorduncu satir.\n'
# >>> f.readlines()[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> f.readlines()[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> satirlar[3]
# 'dorduncu satir.\n'
# >>> f
# <open file 'msg.txt', mode 'r' at 0x100769660>
# >>> f.close()
# >>> f.closed
# True
# >>> f.seek(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file
# >>> 