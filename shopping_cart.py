#Shoping Cart System

cart = [
    {"name": "Apply", "price": 50, "quantity": 2},
    {"name": "Banana", "price": 20, "quantity": 3},
    {"name": "Orange", "price": 70, "quantity": 5},
    {"name": "milk", "price": 20, "quantity": 7},
    {"name": "pen", "price": 10, "quantity": 1}
]

print("\n" + "=" * 40)
print("SHOPPING CART SUMMARY")
print("=" * 40)

print("Shopping Cart Items:")
for item in cart:
    print(item["name"], "-", item["price"])

#calculate total cart price

total_price = 0

for item in cart:
    item_total = item["price"] * item["quantity"]
    total_price = total_price + item_total

print("\nShopping Cart Item:")
for item in cart:
    item_total = item["price"] * item["quantity"]
    print(
        f"{item["name"]:10} | "
        f"Price: {item["price"]:3} | "
        f"Qty: {item["quantity"]:2} | "
        f"Total: ₹{item_total}"
    )

print("-" * 40)
print(f"Grand Total: {total_price}")


#Remove an Item form Cart 

item_to_remove = "Banana"

for item in cart:
    if item["name"] == item_to_remove:
        cart.remove(item)
        break
new_total_price = 0
print("\nUpdated Items:")
for item in cart:
    item_total = item["price"] * item["quantity"]
    new_total_price = new_total_price + item_total
    print(f"{item["name"]:7} - {item["price"]} | Qty - {item['quantity']} | Total - {item_total} ")

print(f"Grand Total: {new_total_price}")
