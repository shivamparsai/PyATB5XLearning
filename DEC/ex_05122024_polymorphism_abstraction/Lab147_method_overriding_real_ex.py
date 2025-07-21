## Important

class OldBrowser:
    def startBrowser(self):
        print("start IE browser")

    def closeBrowser(self):
        print("close IE browser")

class Chrome(OldBrowser):
    def startBrowser(self):
        super().startBrowser()  # calling parent class method
        print("start chrome browser")

    def closeBrowser(self):
        print("close chrome browser")
    pass

chrome = Chrome()
chrome.startBrowser()
chrome.closeBrowser()

# oldbr = OldBrowser()
# oldbr.startBrowser()
