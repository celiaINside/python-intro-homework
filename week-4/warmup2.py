student = {"name": "Corie", "grade": 8, "subjects": ["Math", "Art", "History"]}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False

print(student)