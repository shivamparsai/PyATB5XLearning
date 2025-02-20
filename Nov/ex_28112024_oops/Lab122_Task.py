class student:
    def __init__(self, name, rollno, class1, group, height, age):
        self.name = name
        self.rollno = rollno
        self.class1 = class1
        self.group = group
        self.height = height
        self.age = age

    def student_personal_info(self):
        return print(f"name is {self.name}")

    def student_school_info(self):
        print("class is ", self.class1)
        print(f"rollno  is {self.rollno}")
        print(f"group is {self.group}")

    def student_height_age(self):
        print("height is ", self.height)
        print("age is ", self.age)


st = student("shivam", 1212, "12th", "A", 5.6, 31)

st.student_personal_info()
st.student_school_info()
st.student_height_age()