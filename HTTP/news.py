import requests
import requests

headlines_url = "https://newsapi.org/v2/top-headlines"
apiKey = "asdfasdfa"

response = requests.get(headlines_url, params={
    "apiKey": apiKey,
    "country": "tr"
})

news = response.json()
sonuc = news
sonuc = news["articles"][0]["source"]['name']

for i in news["articles"]:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])

# print(sonuc)