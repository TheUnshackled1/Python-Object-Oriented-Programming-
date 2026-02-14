student_grades = {
    "Lebron": 85,
    "Kobe": 92,
    "Jordan": 78
}
print("Original dictionary:", student_grades)

student_grades["Shaq"] = 90
print("After adding Shaq:", student_grades)

student_grades["Lebron"] = 95
print("After updating Lebron's grade:", student_grades)

print("\nAll students and their grades:")
for name, grade in student_grades.items():
    print(f"  {name}: {grade}")
