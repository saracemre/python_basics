import requests

url = "http://hasanadiguzel.com.tr/api/kurgetir"
from_which = input("Bozdurmak istediginiz para birimi: ")
amount = int(input(f"TL'ye donusturmek istediginiz {from_which} miktari: "))


response = requests.get(url)
exchange = response.json()

for i in exchange["TCMB_AnlikKurBilgileri"]:
    if i["Isim"] == from_which:
        print(f"1 {i['Isim']} = {i['ForexSelling']} TL")
        print(f"{amount} {i['Isim']} = {amount*i['ForexSelling']} TL")
 
