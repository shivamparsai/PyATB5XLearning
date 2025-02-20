# find the missing key

dict1 = {"a": 1, "b":2, "c":3}
dict2 = {"a": 1, "b":2}

# missingKey = set(dict1.keys())-set(dict2.keys())
missingKey = dict1.keys() - dict2.keys()

print(missingKey)