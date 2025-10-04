# ### To Load the Variables form the env
# - Install the `pip install python-dotenv`
# - Write the call method at the top.
# `from dotenv import load_dotenv
# import os`
# - call this = `load_dotenv()`
# - Create .env file with data
#     - `EMAIL="<>"`
#     - `PASSWORD="<>"`
#
# - Now you use it
#     - `email = os.getenv("EMAIL")`
#     - `password = os.getenv("PASSWORD")`
#below data to use in file .env file
#EMAIL = "admin"
#PASSWORD = "pass123"



from dotenv import load_dotenv
import os

class LoginPage:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == email1 and self.password == password1:
            print("login success")
        else:
            print("login failed")

load_dotenv()
email1 = os.getenv("email")
password1 = os.getenv("password")

print(email1,password1)

email1 = input("what is your email\n")
password1 = input("what is your password\n")

lp = LoginPage(email1, password1)
lp.login_confirm()
