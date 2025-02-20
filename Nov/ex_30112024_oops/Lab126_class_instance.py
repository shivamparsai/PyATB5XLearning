class person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name

amit = person("amit")
shivam = person("shivam")

print(amit.name)
print(shivam.name)

print("who is walking "+ amit.walk())
print("who is walking "+ shivam.walk())
