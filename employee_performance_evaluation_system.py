# ============================================================
# Module: Week 2 Final Test
# Assignment: Employee Performance Evaluation System
# ============================================================

print("=" * 70)
print("          EMPLOYEE PERFORMANCE EVALUATION SYSTEM")
print("=" * 70)

# ------------------------------------------------------------
# 1. Accept Employee Details
# ------------------------------------------------------------

employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")
department = input("Enter Department: ")

# ------------------------------------------------------------
# 2. Accept Performance Scores
# ------------------------------------------------------------

productivity = float(input("Enter Productivity Score (0-100): "))
communication = float(input("Enter Communication Score (0-100): "))
technical_skills = float(input("Enter Technical Skills Score (0-100): "))
teamwork = float(input("Enter Teamwork Score (0-100): "))
attendance = float(input("Enter Attendance Score (0-100): "))

# ------------------------------------------------------------
# 3. Calculate Total and Average Score
# ------------------------------------------------------------

total_score = (
    productivity
    + communication
    + technical_skills
    + teamwork
    + attendance
)

average_score = total_score / 5

# ------------------------------------------------------------
# 4. Determine Performance Rating
# ------------------------------------------------------------

if average_score >= 90:
    performance_rating = "Excellent"
elif average_score >= 75:
    performance_rating = "Very Good"
elif average_score >= 60:
    performance_rating = "Good"
elif average_score >= 50:
    performance_rating = "Average"
else:
    performance_rating = "Needs Improvement"

# ------------------------------------------------------------
# 5. Determine Promotion Eligibility
# ------------------------------------------------------------

promotion_eligible = (
    average_score >= 75
    and attendance >= 80
)

# ------------------------------------------------------------
# 6. Determine Performance Bonus Eligibility
# ------------------------------------------------------------

bonus_eligible = (
    average_score >= 70
    and productivity >= 70
    and teamwork >= 70
)

# ------------------------------------------------------------
# 7. Determine Training Requirement
# ------------------------------------------------------------

scores = [productivity, communication, technical_skills, teamwork, attendance]

# Membership operator: 'in'
training_required = (
    50 in scores
    or any(score < 60 for score in scores)
)

# ------------------------------------------------------------
# 8. Display Complete Performance Report
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("             EMPLOYEE PERFORMANCE REPORT")
print("=" * 70)

print(f"Employee ID          : {employee_id}")
print(f"Employee Name        : {employee_name}")
print(f"Department           : {department}")

print("-" * 70)

print(f"Productivity         : {productivity:.2f}")
print(f"Communication        : {communication:.2f}")
print(f"Technical Skills     : {technical_skills:.2f}")
print(f"Teamwork             : {teamwork:.2f}")
print(f"Attendance           : {attendance:.2f}")

print("-" * 70)

print(f"Total Score          : {total_score:.2f} / 500")
print(f"Average Score        : {average_score:.2f} / 100")
print(f"Performance Rating   : {performance_rating}")

print("-" * 70)

if promotion_eligible:
    print("Promotion Eligibility : ELIGIBLE")
else:
    print("Promotion Eligibility : NOT ELIGIBLE")

if bonus_eligible:
    print("Bonus Eligibility     : ELIGIBLE")
else:
    print("Bonus Eligibility     : NOT ELIGIBLE")

if training_required:
    print("Training Requirement  : TRAINING REQUIRED")
else:
    print("Training Requirement  : NO TRAINING REQUIRED")

print("=" * 70)
print("          Performance Evaluation Completed")
print("=" * 70)
