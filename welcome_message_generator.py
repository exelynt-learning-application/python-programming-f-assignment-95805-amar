# ============================================================
# Module: String Data Type
# Assignment: Welcome Message Generator
# ============================================================

print("=" * 65)
print("\tPERSONALIZED WELCOME MESSAGE GENERATOR")
print("=" * 65)

# Accept user details
user_name = input("Enter your name: ")
city = input("Enter your city: ")
course_name = input("Enter your course name: ")
college_name = input("Enter your college name: ")

# ------------------------------------------------------------
# String concatenation
# ------------------------------------------------------------

student_info = user_name + " from " + city

# ------------------------------------------------------------
# Multi-line string and f-string formatting
# ------------------------------------------------------------

welcome_message = f"""
Dear {user_name},

\tCongratulations and welcome to {college_name}!

We are pleased to confirm your enrollment in the
{course_name} course.

Student Details:
\tName    : {user_name}
\tCity    : {city}
\tCourse  : {course_name}
\tCollege : {college_name}

We are excited to have you join our academic community.
We wish you great success in your educational journey!

\tRegards,
\tAdmissions Department
\t{college_name}
"""

# ------------------------------------------------------------
# Display final formatted welcome message
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("\t\tWELCOME MESSAGE")
print("=" * 65)

print(welcome_message)

print("=" * 65)
print("\tThank you for choosing our institution!")
print("=" * 65)
