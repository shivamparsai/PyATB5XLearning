from Browser_Package.Open_Browser import openBrowser
from Browser_Package.Close_Browser import closeBrowser

class Testcase:
    def testcase(self):
        openBrowser()
        closeBrowser()

tc = Testcase()
tc.testcase()