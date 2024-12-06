# Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
# Kullanimi: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => Dosyayi hangi amacla actigimizi belirtir.
# "r": okuma modu => belirtilen konumda dosya olmalidir.

f = open('msg.txt')
print(f)
# print(help(f))
print(f.read())



