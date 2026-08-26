# ============================================================
# Module: Comparison and Logical Operators
# Assignment: Scholarship Eligibility System
# ============================================================

print("=" * 65)
print("             SCHOLARSHIP ELIGIBILITY SYSTEM")
print("=" * 65)

# ------------------------------------------------------------
# Accept Student Details
# ------------------------------------------------------------

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
percentage = float(input("Enter Percentage: "))
family_income = float(input("Enter Annual Family Income: ₹"))
attendance = float(input("Enter Attendance Percentage: "))

# ------------------------------------------------------------
# Eligibility Conditions
# ------------------------------------------------------------

percentage_condition = percentage >= 75
income_condition = family_income <= 300000
attendance_condition = attendance >= 80

# All conditions must be True
eligible = percentage_condition and income_condition and attendance_condition

# ------------------------------------------------------------
# Display Scholarship Eligibility Report
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("          SCHOLARSHIP ELIGIBILITY REPORT")
print("=" * 65)

print(f"Student Name          : {student_name}")
print(f"Roll Number           : {roll_number}")
print(f"Percentage            : {percentage:.2f}%")
print(f"Annual Family Income  : ₹{family_income:,.2f}")
print(f"Attendance Percentage : {attendance:.2f}%")

print("-" * 65)

print(f"Percentage >= 75%     : {percentage_condition}")
print(f"Income <= ₹3,00,000   : {income_condition}")
print(f"Attendance >= 80%     : {attendance_condition}")

print("-" * 65)

if eligible:
    print("Scholarship Status    : ELIGIBLE")
    print("Congratulations! You meet all scholarship requirements.")
else:
    print("Scholarship Status    : NOT ELIGIBLE")
    print("You do not meet all the scholarship requirements.")

print("=" * 65)
