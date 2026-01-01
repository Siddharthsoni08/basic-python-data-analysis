#Shoping Cart System

cart = [
    {"name": "Apply", "price": 50},
    {"name": "Banana", "price": 20},
    {"name": "Orange", "price": 70},
    {"name": "milk", "price": 20},
    {"name": "pen", "price": 10}
]

print("Shopping Cart Items:")
for item in cart:
    print(item["name"], "-", item["price"])

#calculate total cart price

total_price = 0

for item in cart:
    total_price = total_price + item["price"]

print("\nTotal Cart Price:")
print("₹", total_price)