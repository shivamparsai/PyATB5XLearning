def sum_three(a=1, b=2, c=3):
    return a+b+c

r = sum_three()
print(r)

r1 = sum_three(2, 5)
print(r1)

r2 = sum_three(5, 5, 5,)
print(r2)

r3 = sum_three(5, 5, 5, 4) # cannot give extra parameter/arg
print(r3)