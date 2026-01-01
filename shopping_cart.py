#Shoping Cart System

cart = [
    {"name": "Apply", "price": 50, "quantity": 2},
    {"name": "Banana", "price": 20, "quantity": 3},
    {"name": "Orange", "price": 70, "quantity": 5},
    {"name": "milk", "price": 20, "quantity": 7},
    {"name": "pen", "price": 10, "quantity": 1}
]

print("Shopping Cart Items:")
for item in cart:
    print(item["name"], "-", item["price"])

#calculate total cart price

total_price = 0

for item in cart:
    total_item = item["price"] * item["quantity"]
    total_price = total_price + total_item

print("\nShopping Cart Item:")
for item in cart:
    print(
        item["name"],
        "- Price:", item["price"],
        "| Quantity:", item["quantity"]
    )

print("\nTotal Cart Price:")
print("₹", total_price)

#Remove an Item form Cart 

item_to_remove = "Banana"

for item in cart:
    if item["name"] == item_to_remove:
        cart.remove(item)
        break

print("\nUpdated Items:")
for item in cart:
    print(item["name"], "-", item["price"])