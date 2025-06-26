class ABC:
    def userInput(self):
        try:
            value = int(input("Enter value"))

        except Exception as e:
            print("give only numeric value")
        else:
            print(value)

abc = ABC()
abc.userInput()
