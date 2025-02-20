# dict from 2 list

keys = ["name", "role", "exp"]
#values = ["shivam", "engineer", 23]
values = ["shivam", "engineer"]

# zip method combine both the list values

dict1 = dict(zip(keys, values))

print(dict1)

# merge 2 dicts

dict2 = {"a": 1, "b": 2}
dict3 = {"c": 3, "d": 4}

# or | operand
mergeDict = dict2 | dict3

print(mergeDict)
print(mergeDict.get("c"))