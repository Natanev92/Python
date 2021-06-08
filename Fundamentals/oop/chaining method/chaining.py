class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        self.account_balance
        return self

guido = User("Guido van Rossum")
monty = User("Monty Python")
natan = User("Natan Villasenor")

guido.make_deposit(50).make_deposit(125).make_deposit(300).make_withdrawl(75)

monty.make_deposit(100).make_deposit(200).make_withdrawl(50).make_withdrawl(50)

natan.make_deposit(1900).make_withdrawl(250).make_withdrawl(250).make_withdrawl(250)

print(guido.account_balance)
print(monty.account_balance)
print(natan.account_balance)