# ============================================================
# Module: Input and Output Operations
# Assignment: Personal Profile Generator
# ============================================================

print("\n" + "=" * 50)
print("           PERSONAL PROFILE GENERATOR")
print("=" * 50)

# 1. Accept Name
name = input("Enter your name: ")

# 2. Accept Age
age = input("Enter your age: ")

# 3. Accept Gender
gender = input("Enter your gender: ")

# 4. Accept City
city = input("Enter your city: ")

# 5. Accept Mobile Number
mobile_number = input("Enter your mobile number: ")

# 6. Accept Email Address
email = input("Enter your email address: ")

# 7. Accept Favorite Programming Language
favorite_language = input("Enter your favorite programming language: ")


# 8. Display formatted profile card
print("\n")
print("=" * 50)
print("              PERSONAL PROFILE")
print("=" * 50)

print(f"Name                 : {name}")
print(f"Age                  : {age}")
print(f"Gender               : {gender}")
print(f"City                 : {city}")
print(f"Mobile Number        : {mobile_number}")
print(f"Email Address        : {email}")
print(f"Favorite Language    : {favorite_language}")

print("=" * 50)
print("       Thank you for using the Profile Generator!")
print("=" * 50)
