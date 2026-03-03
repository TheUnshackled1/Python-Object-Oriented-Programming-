import getpass

accounts = {
    "admin": "admin123",
    "teacher": "teacher123"
}

print("=" * 40)
print("       STUDENT GRADING SYSTEM")
print("=" * 40)

# Login loop
logged_in = False
attempts = 3

while attempts > 0:
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username in accounts and accounts[username] == password:
        print("Login successful! Welcome, " + username + "!")
        logged_in = True
        break
    else:
        attempts = attempts - 1
        print("Invalid username or password. Attempts left: " + str(attempts))

if logged_in == False:
    print("Too many failed attempts. Exiting.")
    exit()

# ----- Storage -----
# List to store all student records
student_records = []

# Set to track unique students (avoid duplicates)
registered_students = set()

# ----- Main Menu Loop -----
running = True

while running:
    print("\n" + "=" * 40)
    print("           MAIN MENU")
    print("=" * 40)
    print("[1] Add Student and Grades")
    print("[2] View All Students")
    print("[3] Search Student")
    print("[4] Exit")
    choice = input("Enter your choice: ")

    # ===== OPTION 1: Add Student =====
    if choice == "1":
        print("\n--- Add Student ---")

        last_name = ""
        while last_name == "":
            last_name = input("Enter Last Name: ")
            if last_name == "":
                print("Last Name cannot be empty. Please try again.")

        first_name = ""
        while first_name == "":
            first_name = input("Enter First Name: ")
            if first_name == "":
                print("First Name cannot be empty. Please try again.")

        # Use a tuple for the student name (immutable)
        student_name = (last_name, first_name)
        full_name = last_name + ", " + first_name

        # Check for duplicate using set
        if full_name in registered_students:
            print("This student is already registered!")
            continue

        # Dictionary to hold all grades for this student
        student_data = {}
        student_data["name"] = student_name
        student_data["full_name"] = full_name

        # ----- Grade Input for MIDTERM and ENDTERM -----
        terms = ["Midterm", "Endterm"]
        term_grades = {}

        for term in terms:
            print("\n--- " + term + " Grades ---")

            # Quiz and Activity (40%)
            quiz_count = int(input("How many quizzes/activities for " + term + "? "))
            quiz_list = []
            for i in range(quiz_count):
                score = float(input("  Enter Quiz/Activity " + str(i + 1) + " grade: "))
                quiz_list.append(score)

            if len(quiz_list) > 0:
                quiz_avg = sum(quiz_list) / len(quiz_list)
            else:
                quiz_avg = 0

            # Project (30%)
            project_count = int(input("How many projects for " + term + "? "))
            project_list = []
            for i in range(project_count):
                score = float(input("  Enter Project " + str(i + 1) + " grade: "))
                project_list.append(score)

            if len(project_list) > 0:
                project_avg = sum(project_list) / len(project_list)
            else:
                project_avg = 0

            # Exam (20%)
            exam_grade = float(input("Enter Exam grade for " + term + ": "))

            # Class Participation (10%)
            participation_grade = float(input("Enter Class Participation grade for " + term + ": "))

            # Compute term grade
            term_grade = (quiz_avg * 0.40) + (project_avg * 0.30) + (exam_grade * 0.20) + (participation_grade * 0.10)

            # Store term details in a dictionary
            term_details = {}
            term_details["quiz_grades"] = quiz_list
            term_details["quiz_avg"] = round(quiz_avg, 2)
            term_details["project_grades"] = project_list
            term_details["project_avg"] = round(project_avg, 2)
            term_details["exam"] = exam_grade
            term_details["participation"] = participation_grade
            term_details["term_grade"] = round(term_grade, 2)

            term_grades[term] = term_details

            print(term + " Grade: " + str(round(term_grade, 2)))

        # ----- Compute Final Grade -----
        midterm_grade = term_grades["Midterm"]["term_grade"]
        endterm_grade = term_grades["Endterm"]["term_grade"]

        final_grade = (midterm_grade * 0.40) + (endterm_grade * 0.60)
        final_grade = round(final_grade, 2)

        # Determine remarks using conditionals
        if final_grade >= 75:
            remarks = "PASSED"
        else:
            remarks = "FAILED"

        student_data["term_grades"] = term_grades
        student_data["final_grade"] = final_grade
        student_data["remarks"] = remarks

        # Add to list and set
        student_records.append(student_data)
        registered_students.add(full_name)

        print("\n" + "=" * 40)
        print("  STUDENT ADDED SUCCESSFULLY!")
        print("=" * 40)
        print("Name: " + full_name)
        print("Midterm Grade: " + str(midterm_grade))
        print("Endterm Grade: " + str(endterm_grade))
        print("Final Grade: " + str(final_grade))
        print("Remarks: " + remarks)

    # ===== OPTION 2: View All Students =====
    elif choice == "2":
        print("\n--- All Student Records ---")

        if len(student_records) == 0:
            print("No students added yet.")
        else:
            count = 1
            for student in student_records:
                print("\n--- Student #" + str(count) + " ---")
                print("Name: " + student["full_name"])

                for term in ["Midterm", "Endterm"]:
                    details = student["term_grades"][term]
                    print("\n  " + term + ":")
                    print("    Quiz/Activity Grades: " + str(details["quiz_grades"]))
                    print("    Quiz/Activity Average: " + str(details["quiz_avg"]))
                    print("    Project Grades: " + str(details["project_grades"]))
                    print("    Project Average: " + str(details["project_avg"]))
                    print("    Exam: " + str(details["exam"]))
                    print("    Participation: " + str(details["participation"]))
                    print("    " + term + " Grade: " + str(details["term_grade"]))

                print("\n  Midterm (40%): " + str(student["term_grades"]["Midterm"]["term_grade"]))
                print("  Endterm (60%): " + str(student["term_grades"]["Endterm"]["term_grade"]))
                print("  FINAL GRADE: " + str(student["final_grade"]))
                print("  REMARKS: " + student["remarks"])
                count = count + 1

    # ===== OPTION 3: Search Student =====
    elif choice == "3":
        print("\n--- Search Student ---")
        search_name = input("Enter student name to search (Last, First): ")

        found = False
        for student in student_records:
            if student["full_name"].lower() == search_name.lower():
                found = True
                print("\n--- Student Found ---")
                print("Name: " + student["full_name"])

                for term in ["Midterm", "Endterm"]:
                    details = student["term_grades"][term]
                    print("\n  " + term + ":")
                    print("    Quiz/Activity Average: " + str(details["quiz_avg"]))
                    print("    Project Average: " + str(details["project_avg"]))
                    print("    Exam: " + str(details["exam"]))
                    print("    Participation: " + str(details["participation"]))
                    print("    " + term + " Grade: " + str(details["term_grade"]))

                print("\n  FINAL GRADE: " + str(student["final_grade"]))
                print("  REMARKS: " + student["remarks"])
                break

        if found == False:
            print("Student not found.")

    # ===== OPTION 4: Exit =====
    elif choice == "4":
        print("\nThank you for using the Grading System. Goodbye!")
        running = False

    else:
        print("Invalid choice. Please try again.")
