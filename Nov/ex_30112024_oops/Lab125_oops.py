count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()

print(count)