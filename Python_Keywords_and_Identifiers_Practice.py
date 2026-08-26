# ============================================================
# Module: Python Syntax
# Assignment: Python Keywords and Identifiers Practice
# ============================================================

import keyword

# ------------------------------------------------------------
# 1. Create variables using valid identifiers
# ------------------------------------------------------------

student_name = "Amar"
student_age = 20
student_marks = 85.5
is_passed = True

print("1. Valid Identifiers")
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student Marks:", student_marks)
print("Passed:", is_passed)


# ------------------------------------------------------------
# 2. Invalid variable names and their corrections
# ------------------------------------------------------------

print("\n2. Invalid Identifiers and Corrections")

# Invalid:
# 1student = "Amar"        # Cannot start with a number
# student-name = "Amar"    # Hyphen is not allowed
# class = "Python"         # 'class' is a Python keyword
# student name = "Amar"    # Spaces are not allowed

# Correct versions:
student1 = "Amar"
student_name_correct = "Amar"
class_name = "Python"
student_full_name = "Amar Patil"

print("student1 =", student1)
print("student_name_correct =", student_name_correct)
print("class_name =", class_name)
print("student_full_name =", student_full_name)


# ------------------------------------------------------------
# 3. Display the list of Python keywords
# ------------------------------------------------------------

print("\n3. Python Keywords")

print(keyword.kwlist)


# ------------------------------------------------------------
# 4. Difference between keywords and identifiers
# ------------------------------------------------------------

print("\n4. Keywords vs Identifiers")

# Keywords are reserved words in Python.
# Examples: if, else, for, while, class, def, return

# Identifiers are names given to variables, functions, classes, etc.

course_name = "Python"
course_duration = 3

if course_duration > 0:
    print("Course:", course_name)
    print("Duration:", course_duration, "months")

print("Here, 'if' is a keyword.")
print("'course_name' and 'course_duration' are identifiers.")


# ------------------------------------------------------------
# 5. Different naming conventions
# ------------------------------------------------------------

print("\n5. Naming Conventions")

# snake_case - commonly used for variables and functions
student_name_snake = "Amar Patil"

# PascalCase - commonly used for classes
class StudentDetails:
    pass

# camelCase - possible in Python, but not the recommended
# standard for variables according to PEP 8
studentNameCamel = "Amar Patil"

print("snake_case:", student_name_snake)
print("PascalCase:", StudentDetails.__name__)
print("camelCase:", studentNameCamel)


# ------------------------------------------------------------
# 6. Descriptive variable names for student information
# ------------------------------------------------------------

print("\n6. Student Information")

student_name = "Amar Patil"
student_roll_number = 101
student_age = 20
student_course = "Computer Science"
student_marks = 88.5

print("Student Name:", student_name)
print("Roll Number:", student_roll_number)
print("Age:", student_age)
print("Course:", student_course)
print("Marks:", student_marks)


# ------------------------------------------------------------
# 7. Program following Python naming conventions
# ------------------------------------------------------------

print("\n7. Python Naming Conventions Example")

first_name = "Amar"
last_name = "Patil"
student_age = 20
math_marks = 85
python_marks = 92

total_marks = math_marks + python_marks
average_marks = total_marks / 2

print("Name:", first_name, last_name)
print("Age:", student_age)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if average_marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")


# ============================================================
# Naming Conventions and Keywords - Explanation
# ============================================================

print("\n--- Naming Conventions ---")
print("1. Variables and functions should normally use snake_case.")
print("2. Classes should normally use PascalCase.")
print("3. Constants are commonly written in UPPER_CASE.")
print("4. Identifiers should be meaningful and descriptive.")
print("5. Identifiers cannot start with a number.")
print("6. Spaces and special characters are not allowed in identifiers.")
print("7. Python keywords cannot be used as identifiers.")

print("\n--- Examples of Python Keywords ---")
print("if, else, for, while, class, def, return, import, True, False")
