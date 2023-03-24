class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance
        pass

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        pass
    
a = Account("Ashish", 5000)
print(a.title)     # "Ashish"
print(a.balance)   # 5000

sa = SavingsAccount("Ashish", 5000, 5)
print(sa.title)          # "Ashish"
print(sa.balance)        # 5000
print(sa.interestRate)   # 5
