from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")


sonuc = obj.find("div")
sonuc = obj.find_all("div") # liste seklinde verir.
sonuc = len(obj.find_all('div'))
sonuc = obj.find_all("div")[0] 
sonuc = obj.find_all("div")[0].ul
sonuc = obj.find_all("div")[0].ul.li
sonuc = obj.find_all("div")[0].ul.find_all("li")
sonuc = obj.find_all("div")[0].ul.find_all("li")[1]

divs = obj.find_all("div")

# for div in divs:
#     if div.h2.a != None:
#         print(div.h2.a.string.strip())
#     else:
#         print(div.h2.string.strip())

for a in obj.find_all('a'):
    print(a.string)
    

# print(sonuc)

