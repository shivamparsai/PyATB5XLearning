# main method - but rarely used

def main():
    print("Main Method")

# if __name__ == "__main__":  # main method is line no. 1
#     main()

# multiple main method is also possible - below is the another main

def test():
    print("this is 2nd main method")

# if __name__ == "__main__":
#     test()

def test2():
    print("This is 3rd main method")

if __name__ == "__main__":
    main()
    test()