# Program - if age is > 18, then allowed to vote
# else, not allowed

userAge = int(input("Enter your age \n"))

if userAge > 18:
    print("You are allowed to vote")
else:
    print("You are under 18, can not cast vote")

# or
# but below coding is not suggested

print("You are allowed to vote"if userAge > 18 else "You can't vote")
print("You are allowed to give vote"if int(input("Enter your age \n")) > 18 else "You can't vote")