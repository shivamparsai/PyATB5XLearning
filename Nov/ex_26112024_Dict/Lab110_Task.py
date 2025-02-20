# write a function that returns the max value from a dict

# {"a":10, "b":20, "c":30}

def maxDictValue(dict1):
    return max(dict1.values())
    #return min(dict1.values())

print(maxDictValue({"a":10, "b":20, "c":30}))