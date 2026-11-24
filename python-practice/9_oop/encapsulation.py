class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("amount should be positive")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("not enough money")


acc = Account("Amina", 5000)
print(acc.get_balance())

acc.deposit(1000)
print(acc.get_balance())

acc.withdraw(10000)
acc.withdraw(2000)
print(acc.get_balance())

print(acc._Account__balance)
