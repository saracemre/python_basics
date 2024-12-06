import os 
import datetime

result = dir(os)

result = os.name


# Dizin degistirme
# os.chdir('C:\\')
# os.chdir('../..')

# Klasor olusturma
# os.mkdir('newdirectory') # Ayni dizinin icerisinde klasor olusturur.
# os.makedirs("newdirectory/yeniklasor")
# os.rename('newdirectory','yeniklasor')
# os.rmdir('newdirectory') # Alt klasoru olmayan klasoru silmek icin kullanilir.
# os.removedirs('yeniklasor/yeniklasor') # Alt klasoru olan klasoru silmek icin kullanilir.



# Listeleme
# result = os.listdir()
# reulst = os.listdir('C:\\')

# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)



# Etkin dizin ogrenme
# result = os.getcwd()


# result = os.stat("datetime_module.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # Olusturulma tarihi(creat)
# result = datetime.datetime.fromtimestamp(result.st_atime) # Son erisim tarihi(acces)
# result = datetime.datetime.fromtimestamp(result.st_mtime)   # Degistirilma tarihi(modify)

# os.system('notepad.exe') # Istenilen dosyayi acar.

# path

result = os.path.abspath('os_module.py')
result = os.path.dirname('/Users/emresarac/python_temelleri/Module/os_module.py')
result = os.path.dirname(os.path.abspath('os_module.py'))
result = os.path.exists('os_module.py') # Var mi diye sorar
result = os.path.isdir('/Users/emresarac/python_temelleri/Module') # Klasor(dizin) mu diye sorar
result = os.path.isfile('/Users/emresarac/python_temelleri/Module/os_module.py') # Dosya mi diye sorar
result = os.path.join('deneme','deneme1','deneme2') 
result = os.path.split('deneme:\\deneme')
result = os.path.splitext('os_module.py')
# result = result[0]
result = result[1]



print(result)