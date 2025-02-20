cities = ("London", "Paris", "LA", "Tokyo")
print("Paris" in cities)
print("Banglore" in cities)

t = (1, 2, 3)

print(t)

#t.append(12)    # error - AttributeError: 'tuple' object has no attribute 'append'

q = list(t)
q.append(4)

print(q)

t = tuple(q)

print(t)