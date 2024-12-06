from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")


sonuc = obj.find(id="div2")
sonuc = obj.find(class_="bolum")
sonuc = obj.find_all(class_="bolum")[1]

sonuc = obj.select('#header') # liste olarak getirir.
sonuc = obj.select('#div1')
sonuc = obj.select('.bolum')
sonuc = obj.select('.bolum')[1]

sonuc = obj.select_one('.bolum') # buldugu ilk elemani getirir.


sonuc = obj.div.attrs
sonuc = obj.div.attrs['id']
sonuc = obj.div.attrs['class']

sonuc = obj.get_text() # butun textleri getirir.
sonuc = obj.get_text(strip=True, separator=",")

for a in obj.find_all('a'):
    # print(a.get('href'))
    print(a['href'])

print(sonuc)
