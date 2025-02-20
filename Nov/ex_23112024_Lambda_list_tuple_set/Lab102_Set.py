# find the 1st non repeating char in a string using sets
# swiss - w

def firstNonRepeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(firstNonRepeating("swiss"))


