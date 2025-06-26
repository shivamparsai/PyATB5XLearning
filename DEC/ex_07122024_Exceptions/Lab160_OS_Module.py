# OS - this is a powerful module that provides the functions to interact with OS
# like windows, MacOS etc
# File and Directory functions
# current working directory etc

import os

print(os.getcwd())  # cwd - current working directory

# list files in the current directory
files = os.listdir('C:/Users/DELL/PycharmProjects/PyATB5XLearning/')
print(f"Files in the current directory: {files}")

# create the new dir
# os.mkdir("TEST2")   # if path is not given then it will create the folder in the current dir

# check if file exists

fileexists = os.path.exists("TestData.txt")
print(fileexists)

print(os.name)  # will return nt  = means windows, for Mac it will be posix