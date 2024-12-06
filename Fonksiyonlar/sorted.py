sayilar = [1,53,45,67,97,5,7]

# sayilar.sort()
sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((1,53,45,67,97,5,7))

users = [
    {"username":"emresarac", "tweets":["tweet1","tweet2"],'email':'info@gmail.com'},
    {"username":"mustafasarac", "tweets":[]},
    {"username":"beyzasarac", "tweets":["tweet1"],'name':'','phone':'4747463'}
]

sonuc = sorted(users, key=len)
sonuc = sorted(users, key=len, reverse=True)
sonuc = sorted(users, key=lambda user: user['username'])
sonuc = sorted(users, key=lambda user: len(user['tweets']))




print(sonuc)