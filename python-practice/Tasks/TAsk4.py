class DigitalWallet:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")

    def spend_money(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")


wallet = DigitalWallet("Ayesha", 50)
wallet.spend_money(100)        
wallet.add_money(25)
print(wallet.get_balance())    
