import os

# full_path = os.getcwd()
# print(full_path)
#
# full_path = full_path+"\example.txt"
#
# print(full_path)

# reading the file
# file.open((path or name of the file), "mode")
# mode - read, write, execute

#   'r' open for reading (default)
#   'w' open for writing, truncating the file first
#   'x' create a new file and open it for writing
#   'a' open for writing, appending to the end of the file if it exists
#   'b' binary mode
#   't' text mode (default)
#   '+' open a disk file for updating (reading and writing)

# file = open(full_path)  #FileNotFoundError:

#   use try except

try:
    full_path = os.getcwd()
    print(full_path)

    full_path = full_path+"\example.txt"

    print(full_path)

    file = open(full_path)

except Exception as e:
    print("File not found, fix the path or create the file")
