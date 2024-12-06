# x = int(input('x:'))
# y = int(input('y:'))

# sonuc = (x > y)

# a = int(input('a:'))

# if (a % 2) == 0:
#     print('a sayisi cifttir')

# if (a % 2) == 1:
#     print('a sayisi tektir')

# if a < 0:
#     print('a sayisi negatiftir')

# if a > 0:
#     print('a sayisi pozitiftir')

# print(sonuc)

# vize1 = float(input('1. vize notu:'))
# vize2 = float(input('2. vize notu:'))
# final = float(input('final notu:'))

# ort = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

# if ort >= 50:
#     print('Gecti')

# if ort < 50:
#     print('Kaldi')

_email = 'info@sadikturan.com'
_password = '12345'

email = input('email: ')
password = input('password: ')

isEmail = (email.lower().strip() == _email)
isPassword = (password == _password)

print(f"Mail dogrulugu: {isEmail} ve parola dogrulugu: {isPassword}")