student_info1 = {
    "name": "shivam",
    "age": 32,
    "address":{
        "ofc add": "Outer ring road",
        "home add": "Gunjur"
    }
}

student_info2 = {
    "name": "Dharinee",
    "age": 31,
    "address":{
        "ofc add": "US",
        "home add": "UK"
    }
}

print(student_info2)

print(student_info2["address"]["home add"])

student_info2["address"]["ofc add"] = "LA"

print(student_info2)

#taking dict into list

student_list = [student_info1, student_info2]
print(student_list)
print(student_list[0]["address"]["ofc add"])
print(student_list[1]["age"])

# for i in student_list:
#     print(i)