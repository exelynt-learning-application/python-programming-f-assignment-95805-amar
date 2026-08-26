# ============================================================
# Module: Numbers and Type Conversion
# Assignment: Weight Conversion System
# ============================================================

print("=" * 55)
print("             WEIGHT CONVERSION SYSTEM")
print("=" * 55)

# Accept weight from the user
weight_input = input("Enter weight value: ")

# Convert input string to float
weight = float(weight_input)

print("\nSelect a conversion:")
print("1. Kilograms to Grams")
print("2. Grams to Kilograms")
print("3. Kilograms to Pounds")
print("4. Pounds to Kilograms")

choice = input("\nEnter your choice (1-4): ")

# Perform selected conversion
if choice == "1":
    converted_weight = weight * 1000
    from_unit = "Kilograms"
    to_unit = "Grams"

elif choice == "2":
    converted_weight = weight / 1000
    from_unit = "Grams"
    to_unit = "Kilograms"

elif choice == "3":
    converted_weight = weight * 2.20462
    from_unit = "Kilograms"
    to_unit = "Pounds"

elif choice == "4":
    converted_weight = weight / 2.20462
    from_unit = "Pounds"
    to_unit = "Kilograms"

else:
    print("\nInvalid choice. Please select a number from 1 to 4.")
    exit()

# Display result
print("\n")
print("=" * 55)
print("                 CONVERSION RESULT")
print("=" * 55)

print(f"Original Weight   : {weight:.2f} {from_unit}")
print(f"Converted Weight  : {converted_weight:.2f} {to_unit}")

print("-" * 55)

# Display data types
print(f"Input Data Type   : {type(weight)}")
print(f"Result Data Type  : {type(converted_weight)}")

print("=" * 55)
print("          Weight conversion completed!")
print("=" * 55)
