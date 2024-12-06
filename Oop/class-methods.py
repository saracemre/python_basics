class User:

    active_users = 0 

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanici var."
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)

    def __init__(self, first, last, age):
        print(self)
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan cikis yapti."

# print(User.display_active_users())
# userA = User("Emre", "Sarac", 18)
# userB = User("Musti", "Sarac", 51)
# userC = User("Beyza", "Sarac", 23)


Elif = User.from_string("Elif,Sarac,20")
print(Elif.first)
print(Elif.last)
print(Elif.age)

# {"key": "value"}
# dict.fromkeys()