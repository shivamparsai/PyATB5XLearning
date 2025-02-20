# remove duplicate values from dict

my_dict = {"a":1, "b":2, "c":1, "d":3, "e":4, "f":3}
# o/p - {"a":1, "b":2, "d": 3}

unique_value = set()

result = {}

for key,value in my_dict.items():
    if value not in unique_value:
        unique_value.add(value)
        result[key] = value


print(result)
