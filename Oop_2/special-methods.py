class Film:
    def __init__(self, baslik, yonetmen, sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure

    def __str__(self):
        return f"{self.baslik}, {self.yonetmen} tarafindan yonetildi."

    def __repr__(self):
        return f"{self.baslik}, {self.yonetmen} tarafindan yonetildi."

    def __len__(self):
        return self.sure

    def __del__(self):
        print("film objesi silindi.")


f = Film('Inception', "Christopher Nolan", 148)

print(str(f))
print(f)
print(len(f))

del f