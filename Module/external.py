from termcolor import colored


# sonuc = dir(termcolor)
# sonuc = help(termcolor)

sonuc = colored('Merhaba', color='yellow', on_color='on_blue')
sonuc = colored('Merhaba', color='yellow', on_color='on_blue', attrs=['bold'])



print(sonuc)