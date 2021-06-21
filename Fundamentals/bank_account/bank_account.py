class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        self.int_rate().balance()
        return self
    def yield_interest(self):
        self.balance += (self.balance *self.int_rate)
ba1 = BankAccount(.01, 7600)
ba2 = BankAccount(.01, 4200)
ba1.deposit(120).deposit(1000).deposit(280).withdraw(700).yield_interest()
print(ba1.balance)
ba2.deposit(120).deposit(400).withdraw(500).withdraw(250).yield_interest()
print(ba2.balance)
