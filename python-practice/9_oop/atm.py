class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 10000
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
1. create pin
2. withdraw money
3. exit
""")
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.withdraw()
            else:
                print("bye")
                break

    def create_pin(self):
        self.pin = input("enter new pin: ")
        print("pin created")

    def withdraw(self):
        if self.pin == "":
            print("create a pin first")
            return
        pin = input("enter pin: ")
        if pin == self.pin:
            amount = int(input("enter amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("withdraw successful, balance is", self.balance)
            else:
                print("not enough balance")
        else:
            print("wrong pin")


atm = ATM()
