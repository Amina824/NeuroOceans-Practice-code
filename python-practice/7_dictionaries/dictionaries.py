student = {"name": "Amina", "roll": 161, "class": "BSCS"}
print(student)

print(student["name"])
print(student.get("roll"))
print(student.get("age"))
print(student.keys())
print(student.values())
print(student.items())

student["city"] = "Lahore"
student.update({"age": 20})
print(student)

student["class"] = "BSIT"
print(student)

del student["age"]
student.pop("city")
print(student)

marks = {"math": 80, "english": 75, "science": 90}
print(len(marks))
print("math" in marks)
print(max(marks.values()))
print(sum(marks.values()))

for k in marks:
    print(k)

for k, v in marks.items():
    print(k, v)

student.clear()
print(student)
