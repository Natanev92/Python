class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        self.account_balance
    def transfer_money(self, amount):
        self.account_balance += amount
        self.account_balance -= amount

guido = User("Guido van Rossum")
monty = User("Monty Python")
natan = User("Natan Villasenor")

guido.make_deposit(50)
guido.make_deposit(125)
guido.make_deposit(300)
guido.make_withdrawl(75)
guido.display_user_balance()

monty.make_deposit(100)
monty.make_deposit(200)
monty.make_withdrawl(50)
monty.make_withdrawl(50)
monty.display_user_balance()

natan.make_deposit(1900)
natan.make_withdrawl(250)
natan.make_withdrawl(250)
natan.make_withdrawl(250)
natan.display_user_balance()


print(guido.account_balance)
print(monty.account_balance)
print(natan.account_balance)

guido.transfer_money(natan, 150)
print(guido.account_balance)
print(natan.account_balance)