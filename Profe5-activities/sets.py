# Basic Set Syntax

# 1. Create a set of unique grade values from a dictionary
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 90}
unique_grades = set(student_grades.values())
print("Unique grades:", unique_grades)

# 2. Add a duplicate grade and observe that sets ignore duplicates
unique_grades.add(85)
print("After adding duplicate grade 85:", unique_grades)

# 3. Print the set to show unique grades
print("Final set of unique grades:", unique_grades)
