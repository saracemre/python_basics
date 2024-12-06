class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.description = description
        if price >= 0:
            self._price = price
        else:
            raise ValueError("Fiyat icin negatif deger atamasi yapilmaz.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Fiyat icin negatif deger atamasi yapilmaz.")

    @property
    def short_description(self):
        return self.description[:10]



    # def set_price(self, value):
    #     if value >= 0:
    #         self._price = value
    #     else:
    #         raise ValueError("Fiyat icin negatif deger atamasi yapilmaz.")

    # def get_price(self):
    #     return self._price

p = Product("IPhone 12", 9000, "iphone 12 apple'in cikardigi en yeni urundur ancak fiyati cok pahalidir.")
print(p.price)
# p.price = -9000 
print(p.price)
print(p.short_description)
