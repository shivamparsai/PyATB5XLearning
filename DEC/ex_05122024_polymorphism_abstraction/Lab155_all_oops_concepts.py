from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance, acc_num):
        self.__balance = balance
        self.acc_num = acc_num

    def show_bal(self):
        print(self.__balance)

class ICICI(BankAccount):
    def withdraw(self):
        print("Yes")

    @abstractmethod
    def loan(self):
        pass

    @staticmethod
    def callCustomerCare():
        print("calling")

class Operation(ICICI):
    def loan(self):
        print("Loan")
        self.callCustomerCare()
        self.withdraw()
        print(self.acc_num)
        self.show_bal()

op = Operation(12,1222)
op.loan()