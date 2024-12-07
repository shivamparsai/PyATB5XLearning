# Match statement -> Switch in Java
# Match the o/p and execute
# only in python 3.10 and above

# Match variable:
#     case pattern 1:
#         code block
# case pattern 1:
#         code block


# Write the program to ask the user which browser he/she wants to run the automation

browser_name = input("Enter the browser name\n")
match browser_name:
    case "firefox":
        print("Starting Firefox")
    case "chrome":
        print("Starting chrome")
    case "edge":
        print("starting edge")
    case a:
        print("no browser found")
