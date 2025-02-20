# web automation  - selenium
# page - we are going to automate

from dotenv import load_dotenv
import os

class LoginPage:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "shivam@gmail.com" and self.password == "pass123":
            print("login success")
        else:
            print("login failed")

load_dotenv()
email1 = os.getenv("email")
password1 = os.getenv("password")

print(email1,password1)

lp = LoginPage(email1, password1)
lp.login_confirm()
