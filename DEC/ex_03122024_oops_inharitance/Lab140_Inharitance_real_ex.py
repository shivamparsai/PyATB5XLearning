class BaseTest:
    def openBrowsesr(self):
        print("open browser")

    def closeBrowser(self):
        print("close browser")

class TestCase1(BaseTest):
    def testPositive(self):
        self.openBrowsesr()
        print("Execute test case 1 positive")
        self.closeBrowser()

    def testNegative(self):
        self.openBrowsesr()
        print("Execute test case 1 negative")
        self.closeBrowser()

class TestCase2(BaseTest):
    def testPerformance(self):
        self.openBrowsesr()
        print("Performance test done")
        self.closeBrowser()



testcase1 = TestCase1()

testcase1.testPositive()
testcase1.testNegative()

testcase2 = TestCase2()

testcase2.testPerformance()