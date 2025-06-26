fileName = "shivam.txt"
content = "This is shivem's file"

# write the file
with open(fileName, 'w') as file:
    file.write(content)

# read the file
with open(fileName, 'r') as file:
    print(file.read())