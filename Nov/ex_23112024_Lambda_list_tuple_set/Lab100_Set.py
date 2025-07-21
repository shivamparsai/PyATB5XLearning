# Important

set1 = {1,2,3}
set2 = {3,4,6}

mySet = set1.union(set2)    # it will remove duplicate values and return only unique values from the multiple matrics
print(mySet)
mySet1 = set1.intersection(set2)    # it will return the duplicate values from the multiple matrics
print(mySet1)
mySet3 = set1.difference(set2)      # it will remove the duplicate values and return the remaining values that are not in another set
print(mySet3)
mySet4 = set2.difference(set1)
print(mySet4)


