import requests
from bs4 import BeautifulSoup
import csv

url = 'http://sadikturan.com'

text = requests.get(url).text

# with open('sadikturan.com.html', 'w') as file:
#     file.write(text)

with open('sadikturan.com.html') as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")

with open('kurslar.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['kurs_resmi', 'kurs_baslik', 'kurs_aciklama', 'udemy_link', 'site_link'])
    for a in obj.find_all(class_='card kurs'):
        csv_writer.writerow([a.img.attrs['src'], a.img.attrs['alt'], a.span.string, a.find(class_="btn btn-sm btn-danger").attrs['href'], url + a.find(class_='btn btn-sm btn-primary').attrs['href']])

