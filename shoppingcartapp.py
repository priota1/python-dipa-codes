print("Welcome to Python Market 🛒\n")
print("Available items:")

items = {
    "apple": 1.29,
    "banana":1.00,
    "peach":1.09
}
for item, price in items.items():
    print(f"{item.title()} - {price}")

cart=[]
while True:
    print("Type the product name to add to cart (or type 'checkout' to finish):")
    produce = input("> ").lower()
    if produce == "checkout":
        break
    elif produce in items:
        cart.append(produce)
        print(f"{produce.title()} added to cart!")
    elif produce == "cart":
        if not cart: 
         print("Your cart is empty.")
        else:
            print("\nCurrent cart:")
            for item in cart:
                print(f"-{item.title()}- ${items[item]:.2f}")
    elif produce == "remove":
        product = input("Enter product to remove: ").lower()
        if product in cart:
            cart.remove(product)
            print(f"{product.title()} removed from cart.")
        else:
            print("Item not in cart.")
    else:
         print("Sorry, that item is not available.")
print("\nYour cart contains:")
total=0
for item in cart:
   print(f"- {item.title()} - ${items[item]}")
   total += items[item]

print(f"Total: ${total:.2f}")
print("Thank you for shopping! 🛒")