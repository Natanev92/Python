from bank_account import BankAccount
class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account += amount
        return self
    def make_withdrawl(self, amount):
        self.account -= amount
        return self
    def display_user_balance(self):
        self.account
        return self

guido = User("Guido van Rossum")
monty = User("Monty Python")
natan = User("Natan Villasenor")

print(guido.account.balance)
print(monty.account.balance)
print(natan.account.balance)