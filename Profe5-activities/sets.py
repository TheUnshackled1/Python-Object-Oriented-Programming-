
student_grades = {"Lebron": 85, "Kobe": 92, "Jordan": 78, "Shaq": 90}
unique_grades = set(student_grades.values())
print("Unique grades:", unique_grades)

unique_grades.add(85)
print("After adding duplicate grade 85:", unique_grades)

print("Final set of unique grades:", unique_grades)
