# custom exception

class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


balance = 100

withdraw = int(input("Enter withdrawal amount\n"))
if withdraw > balance:
    raise CustomException("Balance is low")
else:
    print("Remaining Balance is ", balance-withdraw)