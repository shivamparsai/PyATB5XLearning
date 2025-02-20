# Advanced data structure
# List - collection of items
# Duplicates are allowed
# Multiple different data types are allowed
# stored with index - 0 to len-1
# it is mutable in nature (value can be changed)
# like grocery list - banana, butter, paneer, bread
# 10th marks list - 80,81,75,73

# Syntex - []

myList = [1, 2, 3]       # same types of data types
myList2 = [1, True, 12.4, 'Shivam']

print(myList)
print(len(myList2))
print(myList2[0])
print(myList2[1])
print(myList2[2])
print(myList2[3])
# print(myList2[4])       # error - IndexError: list index out of range

myList[0] = 'Shivam'
myList[1] = True
myList[2] = 22.22

print(myList)


for i in myList:
    print(i)

for i in range(1,5):    # range(start, stop-1)
    print(i)

# range(1,5) - returns list [1,2,3,4]