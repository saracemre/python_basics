import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "asdfasdf"
response = requests.get(url, params={
    "key": key,
    "q": "istanbul",
    "aqi": "no",
    "lang": "tr"
})

weather = response.json()

# print(weather)
weather_in_where = weather["location"]["name"]
weather_degree = weather["current"]["temp_c"]
weather_date = weather["location"]["localtime"]
weather_text = weather["current"]["condition"]["text"]

print(f"{weather_date} tarihinde {weather_in_where} lokasyonundaki hava {weather_degree}  derece ve {weather_text}.")
