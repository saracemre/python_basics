class Kart:
    def __init__(self, tip, deger):
        self.tip = tip
        self.deger = deger
    
    # def kartGetir(self):
    #     return f"{self.tip} {self.deger}"

    def __repr__(self):
        return f"{self.tip} {self.deger}"

karo3 = Kart('karo', '3')
sinekAs = Kart('sinek', 'A')
# print(karo3.kartGetir())

print(karo3)
print(sinekAs)