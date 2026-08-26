# ============================================================
# Module: Variables and Data Storage
# Assignment: Product Billing System
# ============================================================

print("=" * 50)
print("              PRODUCT BILLING SYSTEM")
print("=" * 50)

# 1. Accept Product Name
product_name = input("Enter product name: ")

# 2. Accept Product Price
product_price = float(input("Enter product price: ₹"))

# 3. Accept Product Quantity
product_quantity = int(input("Enter product quantity: "))

# 4. Calculate subtotal
subtotal = product_price * product_quantity

# 5. Calculate GST at 18%
gst_rate = 18
gst_amount = subtotal * gst_rate / 100

# 6. Calculate final payable amount
final_amount = subtotal + gst_amount

# 7. Display formatted bill
print("\n")
print("=" * 50)
print("                 FINAL BILL")
print("=" * 50)

print(f"Product Name       : {product_name}")
print(f"Price per Item     : ₹{product_price:.2f}")
print(f"Quantity           : {product_quantity}")
print("-" * 50)
print(f"Subtotal           : ₹{subtotal:.2f}")
print(f"GST (18%)          : ₹{gst_amount:.2f}")
print("-" * 50)
print(f"Final Payable      : ₹{final_amount:.2f}")
print("=" * 50)
print("          Thank you for your purchase!")
print("=" * 50)
