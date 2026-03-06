import hashlib


class Student:
    # Set to track unique courses registered in the system
    registered_courses = set()

    # Tuple of valid grade categories (immutable)
    GRADE_CATEGORIES = ("Academic Records", "Project", "Exam", "Class Participation")

    # Dictionary of category weights
    CATEGORY_WEIGHTS = {
        "Academic Records": 0.40,
        "Project": 0.30,
        "Exam": 0.20,
        "Class Participation": 0.10
    }

    # Tuple of term weights (Midterm, Endterm)
    TERM_WEIGHTS = (0.45, 0.55)

    def __init__(self, last_name, first_name, middle_name, course, year, section):
        # Student info stored as individual attributes
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.course = course
        self.year = year
        self.section = section

        # Add course to the class-level set of unique courses
        Student.registered_courses.add(course)

        # Dictionary to hold grades per term
        # Structure: { "Midterm": {...}, "Endterm": {...} }
        self.grades = {}

        # List to store computed term grades
        self.term_grades = []

        self.final_grade = 0.0
        self.remarks = ""

    def get_full_name(self):
        """Return full name as a tuple."""
        return (self.last_name, self.first_name, self.middle_name)

    def get_full_name_str(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"

    def get_course_info(self):
        """Return course info as a tuple."""
        return (self.course, self.year, self.section)

    def input_grades(self, term):
        """Input grades for a specific term using dictionaries and lists."""
        print(f"\n{'='*50}")
        print(f"  Entering grades for {term}")
        print(f"  Student: {self.get_full_name_str()}")
        print(f"{'='*50}")

        term_grades = {}

        # I. Academic Records - 40% (Quiz, Oral Quiz, Activity)
        print("\n--- I. Academic Records (40%) ---")
        academic_items = ["Quiz", "Oral Quiz", "Activity"]
        academic_scores = []
        for item in academic_items:
            while True:
                try:
                    score = float(input(f"  Enter {item} grade (0-100): "))
                    if 0 <= score <= 100:
                        academic_scores.append(score)
                        break
                    else:
                        print("  Grade must be between 0 and 100.")
                except ValueError:
                    print("  Invalid input. Please enter a number.")

        # Average of academic items
        academic_avg = sum(academic_scores) / len(academic_scores)
        term_grades["Academic Records"] = round(academic_avg, 2)
        print(f"  Academic Records Average: {term_grades['Academic Records']}")

        # II. Project - 30% (System 60%, Documents 40%)
        print("\n--- II. Project (30%) ---")
        project_items = [("System", 0.60), ("Documents", 0.40)]
        project_weighted = 0
        for item_name, weight in project_items:
            while True:
                try:
                    score = float(input(f"  Enter {item_name} grade [{int(weight*100)}%] (0-100): "))
                    if 0 <= score <= 100:
                        project_weighted += score * weight
                        break
                    else:
                        print("  Grade must be between 0 and 100.")
                except ValueError:
                    print("  Invalid input. Please enter a number.")

        term_grades["Project"] = round(project_weighted, 2)
        print(f"  Project Weighted Average: {term_grades['Project']}")

        # III. Exam - 20%
        print("\n--- III. Exam (20%) ---")
        while True:
            try:
                exam_score = float(input("  Enter Exam grade (0-100): "))
                if 0 <= exam_score <= 100:
                    term_grades["Exam"] = round(exam_score, 2)
                    break
                else:
                    print("  Grade must be between 0 and 100.")
            except ValueError:
                print("  Invalid input. Please enter a number.")
        print(f"  Exam Grade: {term_grades['Exam']}")

        # IV. Class Participation - 10% (Research, Attendance, Certificate)
        print("\n--- IV. Class Participation (10%) ---")
        participation_items = ["Research", "Attendance", "Certificate"]
        participation_scores = []
        for item in participation_items:
            while True:
                try:
                    score = float(input(f"  Enter {item} grade (0-100): "))
                    if 0 <= score <= 100:
                        participation_scores.append(score)
                        break
                    else:
                        print("  Grade must be between 0 and 100.")
                except ValueError:
                    print("  Invalid input. Please enter a number.")

        participation_avg = sum(participation_scores) / len(participation_scores)
        term_grades["Class Participation"] = round(participation_avg, 2)
        print(f"  Class Participation Average: {term_grades['Class Participation']}")

        # Store grades in the dictionary for this term
        self.grades[term] = term_grades

    def compute_term_grade(self, term):
        """Compute weighted grade for a specific term using loops and dictionary."""
        if term not in self.grades:
            print(f"  No grades found for {term}.")
            return 0

        term_data = self.grades[term]
        weighted_total = 0

        # Loop through each category and apply weight
        for category in Student.GRADE_CATEGORIES:
            grade = term_data.get(category, 0)
            weight = Student.CATEGORY_WEIGHTS[category]
            weighted_total += grade * weight

        return round(weighted_total, 2)

    def compute_final_grade(self):
        """Compute final grade using Midterm (45%) and Endterm (55%)."""
        terms = ["Midterm", "Endterm"]
        self.term_grades = []  # List to store each term's computed grade

        for term in terms:
            term_grade = self.compute_term_grade(term)
            self.term_grades.append(term_grade)

        # Midterm * 0.45 + Endterm * 0.55
        midterm_weight, endterm_weight = Student.TERM_WEIGHTS  # Tuple unpacking
        self.final_grade = round(
            self.term_grades[0] * midterm_weight + self.term_grades[1] * endterm_weight, 2
        )

        # Conditionals for remarks
        if self.final_grade >= 75:
            self.remarks = "PASSED"
        else:
            self.remarks = "FAILED"

    def display_grades(self):
        """Display all grades, final grade, and remarks."""
        print(f"\n{'='*60}")
        print(f"  STUDENT GRADE REPORT")
        print(f"{'='*60}")
        print(f"  Name    : {self.get_full_name_str()}")
        course, year, section = self.get_course_info()
        print(f"  Course  : {course} {year}-{section}")
        print(f"{'='*60}")

        terms = ["Midterm", "Endterm"]
        for i, term in enumerate(terms):
            if term in self.grades:
                print(f"\n  --- {term} Grades ---")
                for category in Student.GRADE_CATEGORIES:
                    grade = self.grades[term].get(category, 0)
                    weight = int(Student.CATEGORY_WEIGHTS[category] * 100)
                    print(f"    {category} ({weight}%): {grade}")
                print(f"    Term Weighted Grade: {self.term_grades[i]}")

        print(f"\n{'='*60}")
        midterm_pct = int(Student.TERM_WEIGHTS[0] * 100)
        endterm_pct = int(Student.TERM_WEIGHTS[1] * 100)
        print(f"  Midterm ({midterm_pct}%):  {self.term_grades[0]}")
        print(f"  Endterm ({endterm_pct}%):  {self.term_grades[1]}")
        print(f"  FINAL GRADE : {self.final_grade}")
        print(f"  REMARKS     : {self.remarks}")
        print(f"{'='*60}")


# ============================================================
# Authentication System (Registration & Login)
# ============================================================

class AuthSystem:
    def __init__(self):
        # Dictionary to store registered users: { username: (hashed_password, student_name) }
        self.users = {}

    def _hash_password(self, password):
        """Hash password for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        """Register a new user with username, password, and student name."""
        print(f"\n{'='*50}")
        print("  REGISTRATION")
        print(f"{'='*50}")

        while True:
            username = input("  Enter username: ").strip()
            if not username:
                print("  Username cannot be empty.")
                continue
            if username in self.users:
                print("  Username already exists. Try a different one.")
                continue
            break

        while True:
            password = input("  Enter password: ").strip()
            if not password:
                print("  Password cannot be empty.")
                continue
            if len(password) < 4:
                print("  Password must be at least 4 characters.")
                continue
            break

        while True:
            student_name = input("  Enter student's full name: ").strip()
            if not student_name:
                print("  Student name cannot be empty.")
                continue
            break

        self.users[username] = (self._hash_password(password), student_name)
        print(f"\n  Registration successful! Welcome, {student_name}.")

    def login(self):
        """Authenticate a user. Returns username if successful, None otherwise."""
        print(f"\n{'='*50}")
        print("  LOGIN")
        print(f"{'='*50}")

        for attempt in range(3):
            while True:
                username = input("  Enter username: ").strip()
                if not username:
                    print("  Username cannot be empty.")
                    continue
                break

            while True:
                password = input("  Enter password: ").strip()
                if not password:
                    print("  Password cannot be empty.")
                    continue
                break

            if username in self.users:
                stored_hash, student_name = self.users[username]
                if stored_hash == self._hash_password(password):
                    print(f"\n  Login successful! Welcome back, {student_name}.")
                    return username
            print(f"  Invalid credentials. Attempts left: {2 - attempt}")

        print("  Too many failed attempts.")
        return None


# ============================================================
# Main Program
# ============================================================

def main():
    auth = AuthSystem()
    # Dictionary to store Student objects per user: { username: [Student, ...] }
    student_records = {}

    while True:
        print(f"\n{'='*50}")
        print("  STUDENT GRADING SYSTEM")
        print(f"{'='*50}")
        print("  [1] Register")
        print("  [2] Login")
        print("  [3] Exit")
        print(f"{'='*50}")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            auth.register()

        elif choice == "2":
            username = auth.login()
            if username is None:
                continue

            # Initialize student list for this user if not exists
            if username not in student_records:
                student_records[username] = []

            # Logged-in menu
            while True:
                print(f"\n{'='*50}")
                print("  DASHBOARD")
                print(f"{'='*50}")
                print("  [1] Add Student")
                print("  [2] Input Grades")
                print("  [3] Compute & View Grades")
                print("  [4] View All Students")
                print("  [5] View Registered Courses")
                print("  [6] Logout")
                print(f"{'='*50}")

                action = input("  Enter choice: ").strip()

                if action == "1":
                    # Add a new student
                    print(f"\n{'='*50}")
                    print("  ADD STUDENT INFORMATION")
                    print(f"{'='*50}")
                    last_name = input("  Last Name    : ").strip()
                    first_name = input("  First Name   : ").strip()
                    middle_name = input("  Middle Name  : ").strip()
                    course = input("  Course       : ").strip()
                    year = input("  Year         : ").strip()
                    section = input("  Section      : ").strip()

                    student = Student(last_name, first_name, middle_name, course, year, section)
                    student_records[username].append(student)
                    print(f"\n  Student '{student.get_full_name_str()}' added successfully!")

                elif action == "2":
                    # Input grades for a student
                    students = student_records[username]
                    if not students:
                        print("\n  No students added yet. Please add a student first.")
                        continue

                    print(f"\n  --- Select a Student ---")
                    for idx, s in enumerate(students):
                        print(f"  [{idx + 1}] {s.get_full_name_str()}")

                    while True:
                        try:
                            s_choice = int(input("  Enter student number: "))
                            if 1 <= s_choice <= len(students):
                                break
                            else:
                                print(f"  Please enter a number between 1 and {len(students)}.")
                        except ValueError:
                            print("  Invalid input. Please enter a number.")

                    selected_student = students[s_choice - 1]

                    # Choose term
                    print("\n  --- Select Term ---")
                    print("  [1] Midterm (45%)")
                    print("  [2] Endterm (55%)")
                    while True:
                        t_choice = input("  Enter choice: ").strip()
                        if t_choice == "1":
                            term = "Midterm"
                            break
                        elif t_choice == "2":
                            term = "Endterm"
                            break
                        else:
                            print("  Invalid choice. Please enter 1 or 2.")

                    selected_student.input_grades(term)
                    print(f"\n  {term} grades saved for {selected_student.get_full_name_str()}!")

                elif action == "3":
                    # Compute and display grades
                    students = student_records[username]
                    if not students:
                        print("\n  No students added yet.")
                        continue

                    print(f"\n  --- Select a Student ---")
                    for idx, s in enumerate(students):
                        print(f"  [{idx + 1}] {s.get_full_name_str()}")

                    while True:
                        try:
                            s_choice = int(input("  Enter student number: "))
                            if 1 <= s_choice <= len(students):
                                break
                            else:
                                print(f"  Please enter a number between 1 and {len(students)}.")
                        except ValueError:
                            print("  Invalid input. Please enter a number.")

                    selected_student = students[s_choice - 1]

                    # Check if both terms have grades
                    if "Midterm" not in selected_student.grades or "Endterm" not in selected_student.grades:
                        print("\n  Please input grades for BOTH Midterm and Endterm first.")
                        if "Midterm" not in selected_student.grades:
                            print("  Missing: Midterm grades")
                        if "Endterm" not in selected_student.grades:
                            print("  Missing: Endterm grades")
                        continue

                    selected_student.compute_final_grade()
                    selected_student.display_grades()

                elif action == "4":
                    # View all students using loop
                    students = student_records[username]
                    if not students:
                        print("\n  No students added yet.")
                        continue

                    print(f"\n{'='*60}")
                    print("  ALL REGISTERED STUDENTS")
                    print(f"{'='*60}")
                    for idx, s in enumerate(students):
                        last, first, middle = s.get_full_name()  # Tuple unpacking
                        course, year, section = s.get_course_info()  # Tuple unpacking
                        print(f"  [{idx + 1}] {last}, {first} {middle} - {course} {year}-{section}")
                    print(f"{'='*60}")

                elif action == "5":
                    # Display unique courses using set
                    if Student.registered_courses:
                        print(f"\n  --- Unique Registered Courses (Set) ---")
                        for course in sorted(Student.registered_courses):
                            print(f"    - {course}")
                    else:
                        print("\n  No courses registered yet.")

                elif action == "6":
                    print("\n  Logged out successfully.")
                    break

                else:
                    print("\n  Invalid choice. Please try again.")

        elif choice == "3":
            print("\n  Thank you for using the Student Grading System. Goodbye!")
            break

        else:
            print("\n  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
