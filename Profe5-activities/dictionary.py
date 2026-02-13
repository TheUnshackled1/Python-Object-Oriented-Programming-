# Basic Dictionary Syntax

# 1. Create a dictionary with student names and grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
print("Original dictionary:", student_grades)

# 2. Add a new student with a grade
student_grades["Diana"] = 90
print("After adding Diana:", student_grades)

# 3. Update one student's grade
student_grades["Alice"] = 95
print("After updating Alice's grade:", student_grades)

# 4. Print all student names with their grades
print("\nAll students and their grades:")
for name, grade in student_grades.items():
    print(f"  {name}: {grade}")
