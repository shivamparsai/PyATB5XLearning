# Dict
# Key and Value pair
# A Dictionary is an unordered, mutable, and indexed collection of key value pair in python
# Syntex {}
# to access the value - myDict[key]
# Adding/updating the key value pair - myDict[key] = value
# removing the key - del myDict[key]
# Iterating for key, value in myDict.items()
# dict{} - empty dict can be created
# dict methods - get(), keys(), values(), items(), update(), pop(), clear()

myDict = {
    "name" : "Aman",
    "age" : 30,
    "role" :  "automation engineer",
    "exp": 3
}

print(myDict["age"])

print(myDict)

myDict["role"] = "manual tester"

print(myDict)

del myDict["age"]

print(myDict)

for key,value in myDict.items():
    print(key, "->", value)