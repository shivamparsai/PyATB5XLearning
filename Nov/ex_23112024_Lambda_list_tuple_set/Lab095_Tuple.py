# Tuple - collection of items
# Immutable in nature (value can not change)
# Syntex - ()

myTuple = (1,2,3,4)

print(myTuple)

#myTuple[2] = 7  # TypeError: 'tuple' object does not support item assignment

# List
shoppingList = ["bread", "paneer", "jam"]
print(shoppingList)

shoppingList[1] = "Milk"

print(shoppingList)

# Tuple

domain = ("abc.com", "123.com")
print(domain)
domain_list = list(domain)
print(domain_list)
#domain[0] = "aaa.com"   # TypeError: 'tuple' object does not support item assignment

# real time example

api_urls = ("https://youtube.com", "https://FB.com")
print(api_urls)