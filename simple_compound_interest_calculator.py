# ============================================================
# Module: Arithmetic Operators
# Assignment: Simple and Compound Interest Calculator
# ============================================================

print("=" * 60)
print("       SIMPLE AND COMPOUND INTEREST CALCULATOR")
print("=" * 60)

# Accept input from the user
principal = float(input("Enter Principal Amount: ₹"))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time Period (in years): "))

# ------------------------------------------------------------
# Simple Interest Calculation
# Formula: SI = (P × R × T) / 100
# ------------------------------------------------------------

simple_interest = (principal * rate * time) / 100

# Total amount with Simple Interest
simple_total_amount = principal + simple_interest

# ------------------------------------------------------------
# Compound Interest Calculation
# Compounded annually
# Formula: A = P × (1 + R/100) ** T
# CI = A - P
# ------------------------------------------------------------

compound_total_amount = principal * (1 + rate / 100) ** time

compound_interest = compound_total_amount - principal

# ------------------------------------------------------------
# Display Financial Report
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("                 FINANCIAL REPORT")
print("=" * 60)

print(f"Principal Amount              : ₹{principal:,.2f}")
print(f"Rate of Interest              : {rate:.2f}%")
print(f"Time Period                   : {time:.2f} years")

print("-" * 60)

print(f"Simple Interest               : ₹{simple_interest:,.2f}")
print(f"Total Amount (Simple Interest): ₹{simple_total_amount:,.2f}")

print("-" * 60)

print(f"Compound Interest             : ₹{compound_interest:,.2f}")
print(f"Total Amount (Compound)       : ₹{compound_total_amount:,.2f}")

print("=" * 60)
print("          Calculation Completed Successfully")
print("=" * 60)
