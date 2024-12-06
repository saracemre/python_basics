class NewDict(dict):
    def __repr__(self):
        print('repr metodundan mesaj var.')
        return super().__repr__()

    def __missing__(self, key):
        print('Olmayan key bilgisiniz istiyorsunuz.')

    def __getitem__(self, key):
        print("Bir elemani cagiriyorsunuz.")
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print("listeye eleman ekliyorsunuz.")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("listede eleman arayamazsiniz.")
        return super().__contains__(item)


data = NewDict({"first":"Emre", "last":"Sarac"})

print(data['first'])
data['age']
data['first'] = 'Mustafa'
print(data)

print('a' in data)