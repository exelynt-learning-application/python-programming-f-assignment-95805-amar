# Python Development Environment Setup and Execution
# Assignment: Python Development Environment

import sys

# 1. Print a welcome message
print("==========================================")
print("Welcome to the Python Development Environment!")
print("==========================================")

# 2. Display the current Python version
print("\nPython Version:")
print(sys.version)

# 3. Print the names of five programming languages
print("\nFive Programming Languages:")
languages = ["Python", "Java", "C", "C++", "JavaScript"]

for language in languages:
    print("-", language)

# 4. Display a simple formatted timetable
print("\nSimple Timetable:")
print("------------------------------------------")
print(f"{'Day':<12}{'Subject':<20}{'Time':<10}")
print("------------------------------------------")
print(f"{'Monday':<12}{'Python':<20}{'10:00 AM':<10}")
print(f"{'Tuesday':<12}{'Java':<20}{'11:00 AM':<10}")
print(f"{'Wednesday':<12}{'Database':<20}{'12:00 PM':<10}")
print(f"{'Thursday':<12}{'Web Dev':<20}{'10:00 AM':<10}")
print(f"{'Friday':<12}{'C++':<20}{'11:00 AM':<10}")
print("------------------------------------------")
