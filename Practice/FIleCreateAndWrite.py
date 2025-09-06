import os
from pathlib import Path

# os.mkdir("C:/Users/DELL/Desktop/Pyython_test_files/shivam.txt")

# fileName = "shivam.txt"
content = "shivam"
dir = r"C:\Users\DELL\Desktop\Python_test_files"
filepath = dir+r"\shivam.xls"

if os.path.exists(dir):
    with open(filepath, 'w') as textfile:
        textfile.write(content)
else:
    os.mkdir(dir)
    with open(filepath, 'w') as textfile:
        textfile.write(content)
