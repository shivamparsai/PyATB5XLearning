# count vowel from the string

s = "hello world"

vowels = "aeiou"
vowel_count = 0

for char in s:
    if char in vowels:
        vowel_count += 1

print(vowel_count)