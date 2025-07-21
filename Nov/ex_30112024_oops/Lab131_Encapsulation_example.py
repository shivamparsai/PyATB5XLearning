## Important

class Bank:
    def __init__(self, balance, account_number):
        self.balance = balance  # pubic
        self.__account_number = account_number  # private

    def checkBalance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def show_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("not allowed")

    def __private_method(self):
        print("This is a private method and can only be accessed by class")

    def test(self):
        self.__private_method()

Axis_bank = Bank(100,23243456576)

Axis_bank.checkBalance()

Axis_bank.deposit(100)

Axis_bank.checkBalance()
print(Axis_bank.balance)
# print(Axis_bank.__account_number) # cant access directly
Axis_bank.show_account_number(False) # can be access only through function

# Axis_bank.__private_method()  # cant access outside

Axis_bank.test()