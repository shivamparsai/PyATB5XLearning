def beforeAndAftertestUI(testUI):
    def beforeAfter():
        print("Before testUI()")
        testUI()
        print("After testUI()")
    return beforeAfter()

@beforeAndAftertestUI
def testUI():
    print("I will test this UI")