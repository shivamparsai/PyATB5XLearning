# Tuple within Tuple

hero1 = ("Shivam", "Abhishek")
hero2 = ("Manish", "Manoj")

hero3 = (hero1, hero2)

print(hero3)

print(hero3[0])
print(hero3[1])
print(hero3[0][0])
print(hero3[1][1])
print(hero3[1][0])

# List within List

hero1 = ["Shivam", "Abhishek"]
hero2 = ["Manish", "Manoj"]

hero3 = [hero1, hero2]

print(hero3)

print(hero3[0])
print(hero3[1])
print(hero3[0][0])
print(hero3[1][1])
print(hero3[1][0])