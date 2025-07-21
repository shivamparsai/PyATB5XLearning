## Important

def add(n):
    return n + 10
r = add(10)
print(r)

# with lambda expression

r1 = lambda n : n + 10
print(r1(10))


# multiple args
r2 = lambda a, b : a * b
print(r2(2,4))

r3 = lambda c, d, e : c + d + e
print(r3(1, 1, 1))