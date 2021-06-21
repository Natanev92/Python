from bank_account import BankAccount
class User(BankAccount):
    def __init__(self, name, balance=0, rate=0):
        self.name = name
        # self.account = BankAccount(int_rate=0.02, balance = balance)
        super(User, self).__init__(rate, balance)

    def print_info(self):
        print("="*10 + self.name + "="*10)
        print(self.balance)
        print(self.int_rate)

    def update_rate(self, new_rate):
        self.int_rate= new_rate
        self.print_info()


guido = User("Guido van Rossum", balance=100)
guido.deposit(100)
monty = User("Monty Python")
natan = User("Natan Villasenor")

guido.print_info()
monty.print_info()
natan.print_info()
guido.update_rate(1)
