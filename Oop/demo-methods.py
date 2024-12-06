class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def witdraw(self, amount):
        self.balance -= amount
        return self.balance

hesap = BankAccount("Emre Sarac")

print(hesap.getBalance())
hesap.deposit(1000)
print(hesap.getBalance())
hesap.witdraw(500)
print(hesap.getBalance())
