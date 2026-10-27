student = {
    "name": "Alex",
    "grade": 90,
    "subjects": ["Python", "Data", "Web"]
}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False

print("Updated dictionary:", student)
