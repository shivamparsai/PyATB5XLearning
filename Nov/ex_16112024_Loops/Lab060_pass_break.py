for i in range(0, 10, 1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass

# pass is a placeholder statement that does nothing
# pass is used when statement is syntactically required but no action is needed
# pass can also be used in statement, functions, classes and objects.

# i | condition | o/p
# 0 | 0 == 6 -> False | o/p - nothing will be printed
# 1 | 1 == 6 -> False | o/p - nothing will be printed
# .
# .
# 5 | 5 == 5 -> True | o/p - 5
# 6 | 6 == 6 -> True | o/p - 6
# 7 | 7 == 6 -> False | o/p - nothing will be printed
# .
# .
# 10 | 10 == 6 -> False | o/p - nothing will be printed, for loop completed