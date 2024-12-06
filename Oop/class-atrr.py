class User:

    active_users = 0 

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan cikis yapti."

print(User.active_users)
userA = User("Emre", "Sarac", 18)
userB = User("Musti", "Sarac", 51)
userC = User("Beyza", "Sarac", 23)
print(User.active_users)
print(userC.logout())
print(User.active_users)

# print(userA.full_name())
# print(userB.full_name())