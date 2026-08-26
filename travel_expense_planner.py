# ============================================================
# Module: Week 1 Final Test
# Assignment: Travel Expense Planner
# ============================================================

print("=" * 55)
print("              TRAVEL EXPENSE PLANNER")
print("=" * 55)

# ------------------------------------------------------------
# 1. Accept traveler details
# ------------------------------------------------------------

traveler_name = input("Enter traveler name: ")
destination = input("Enter destination: ")
number_of_days = int(input("Enter number of days: "))

# ------------------------------------------------------------
# 2. Accept travel expenses
# ------------------------------------------------------------

transportation = float(input("Enter transportation expense: ₹"))
hotel = float(input("Enter hotel expense: ₹"))
food = float(input("Enter food expense: ₹"))
miscellaneous = float(input("Enter miscellaneous expenses: ₹"))

# ------------------------------------------------------------
# 3. Calculate total trip cost
# ------------------------------------------------------------

total_trip_cost = transportation + hotel + food + miscellaneous

# Calculate average daily expense
average_daily_expense = total_trip_cost / number_of_days

# ------------------------------------------------------------
# 4. Display formatted travel expense summary
# ------------------------------------------------------------

print("\n")
print("=" * 55)
print("             TRAVEL EXPENSE SUMMARY")
print("=" * 55)

print(f"Traveler Name       : {traveler_name}")
print(f"Destination         : {destination}")
print(f"Number of Days      : {number_of_days}")

print("-" * 55)

print(f"Transportation      : ₹{transportation:.2f}")
print(f"Hotel               : ₹{hotel:.2f}")
print(f"Food                : ₹{food:.2f}")
print(f"Miscellaneous       : ₹{miscellaneous:.2f}")

print("-" * 55)

print(f"Total Trip Cost     : ₹{total_trip_cost:.2f}")
print(f"Average Daily Cost  : ₹{average_daily_expense:.2f}")

print("=" * 55)
print("          Thank you for using the planner!")
print("=" * 55)
