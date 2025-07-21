## Important

myList = [1, 3, 2]

#indexing

print("element at the index 0 - ", myList[0])
print("element at the index 1 - ", myList[1])
print("element at the index 2 - ", myList[2])

# append() - add the object at the end of the list

myList.append(4)

print(myList)

# extend() - add the another list with the existing list at the end

myList.extend([6,5,4,7])

print(myList)

# insert() - add an element at particular index

myList.insert(1, "parsai")

print(myList)

print(len(myList))

# remove() - removes the element

myList.remove(4)   # ValueError: list.remove(x): x not in list

print(myList)

#copy() - can create copy of the list

print(myList.copy())

# sort() -

#myList.sort()      # TypeError: '<' not supported between instances of 'str' and 'int',
                   # because we have different data types, for sorting same data type should be present

myList.remove("parsai")

print(myList)
mylist2 = myList.copy()
mylist2.sort()
print(mylist2)