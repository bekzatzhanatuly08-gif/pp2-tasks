class account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, sum):
        self.balance += sum
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Funds")

a , b = map(int,input().split())
x = account('owner', a)
x.withdraw(b)