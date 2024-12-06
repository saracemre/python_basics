# import datetime
from datetime import datetime
from datetime import timedelta

# result = dir(datetime)
# result = help(datetime)

simdi = datetime.now()
simdi = datetime.today()

result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi, '%Y') # Yil
result = datetime.strftime(simdi, '%y') # Yilin son iki basamagi
result = datetime.strftime(simdi, '%X') # Saat, dakika, saniye
result = datetime.strftime(simdi, '%d') # Tarihteki gun
result = datetime.strftime(simdi, '%A') # Gun ismi
result = datetime.strftime(simdi, '%B') # Ay ismi

result = datetime.strftime(simdi, '%Y %B %A')

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,6,12,30,10)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniyeyi datetime'a cevirir
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = simdi - timedelta(days=10)

print(result)