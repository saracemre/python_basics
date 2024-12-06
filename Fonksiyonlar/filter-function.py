yaslar = [5,12,18,24,45]

def yetiskinMi(x):
    if x<18:
        return False
    else:
        return True
sonuc = list(filter(yetiskinMi, yaslar))
sonuc = list(filter(lambda x: x>=18, yaslar))

sayilar = [0,1,25,6,8,9]
sonuc = list(filter(lambda x: x%2==0, sayilar))

isimler = ['emre','yigit','sena','ada']
sonuc = list(filter(lambda n: n[0]=='e', isimler))

sonuc = list(map(lambda isim: isim.upper(), filter(lambda n: n[0]=='e', isimler)))

users = [
    {'username':'emresarac','tweets': ['tweet1','tweet2']},
    {'username':'mustafasarac','tweets': []},
    {'username':'beyzasarac','tweets': ['tweet1']}

]

sonuc = list(filter(lambda user: len(user['tweets'])>0, users))
sonuc = list(map(lambda user: user['username'],filter(lambda user: len(user['tweets'])>0, users)))

sonuc = [user['username'].upper() for user in users if len(user['tweets'])>0]
print(sonuc)

