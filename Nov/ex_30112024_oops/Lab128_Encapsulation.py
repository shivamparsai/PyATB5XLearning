# web automation  - selenium
# page - we are going to automate

class LoginPage:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "shivam@gmail.com" and self.password == "pass123":
            print("login success")
        else:
            print("login failed")

email1 = input("what is your email\n")
password1 = input("what is your password\n")

lp = LoginPage(email1, password1)
lp.login_confirm()

# lp1 = LoginPage("shivam@gmail.com", "pass123")
# lp1.login_confirm()