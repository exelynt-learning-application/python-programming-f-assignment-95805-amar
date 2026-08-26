# ============================================================
# Module: Python Data Types
# Assignment: Product Inventory Management System
# ============================================================

print("=" * 65)
print("             PRODUCT INVENTORY MANAGEMENT SYSTEM")
print("=" * 65)

# ------------------------------------------------------------
# 1. Store Product Details using suitable data types
# ------------------------------------------------------------

# Integer - Product ID
product_id = 101

# String - Product Name
product_name = "Wireless Keyboard"

# String - Category
category = "Computer Accessories"

# Float - Unit Price
unit_price = 1499.50

# Integer - Available Quantity
available_quantity = 25

# String - Supplier Name
supplier_name = "Tech Supplies Pvt. Ltd."

# Boolean - In Stock Status
in_stock = True

# List - Product Tags (Mutable)
product_tags = ["Wireless", "Keyboard", "USB", "Computer"]

# Dictionary - Product Specifications (Mutable)
product_specifications = {
    "Brand": "TechPro",
    "Connectivity": "Wireless",
    "Battery": "AAA",
    "Warranty": "1 Year"
}

# Tuple - Immutable product information
product_dimensions = (45, 15, 3)  # Length, Width, Height in cm

# ------------------------------------------------------------
# 2 & 3. Display complete product information
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("                  PRODUCT INFORMATION")
print("=" * 65)

print(f"Product ID          : {product_id}")
print(f"Product Name        : {product_name}")
print(f"Category            : {category}")
print(f"Unit Price          : ₹{unit_price:.2f}")
print(f"Available Quantity  : {available_quantity}")
print(f"Supplier Name       : {supplier_name}")
print(f"In Stock            : {in_stock}")
print(f"Product Tags        : {product_tags}")
print(f"Specifications      : {product_specifications}")
print(f"Dimensions (cm)     : {product_dimensions}")

print("=" * 65)


# ------------------------------------------------------------
# 4. Display the data type of every variable
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("                    DATA TYPES")
print("=" * 65)

print(f"product_id             : {type(product_id)}")
print(f"product_name           : {type(product_name)}")
print(f"category               : {type(category)}")
print(f"unit_price             : {type(unit_price)}")
print(f"available_quantity     : {type(available_quantity)}")
print(f"supplier_name          : {type(supplier_name)}")
print(f"in_stock               : {type(in_stock)}")
print(f"product_tags           : {type(product_tags)}")
print(f"product_specifications : {type(product_specifications)}")
print(f"product_dimensions     : {type(product_dimensions)}")

print("=" * 65)


# ------------------------------------------------------------
# 5. Mutable and Immutable Data Types
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("             MUTABLE vs IMMUTABLE DATA TYPES")
print("=" * 65)

# LIST is mutable
print("\nBefore changing product_tags:")
print(product_tags)

product_tags.append("Office")

print("After adding a new tag:")
print(product_tags)

print("\nA list is MUTABLE because its contents can be changed.")


# TUPLE is immutable
print("\nProduct dimensions:")
print(product_dimensions)

print("A tuple is IMMUTABLE because its contents cannot be changed.")

# The following would cause an error:
# product_dimensions[0] = 50


# Dictionary is mutable
print("\nBefore changing specifications:")
print(product_specifications)

product_specifications["Color"] = "Black"

print("After adding Color specification:")
print(product_specifications)

print("\nA dictionary is MUTABLE because its contents can be changed.")


# String is immutable
print("\nProduct name:")
print(product_name)

print("A string is IMMUTABLE because its original value cannot be changed directly.")

print("=" * 65)
print("                    PROGRAM COMPLETE")
print("=" * 65)
