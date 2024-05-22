# print("hello world")

#test01
#test02

# Items list with price
items = {
    '001': {'name': 'Pizza', 'price': 10.00},
    '002': {'name': 'Chips', 'price': 5.00},
    '003': {'name': 'drink', 'price': 2.00},
}

# Start with an empty basket
basket = []

# Function to display the basket
def view_basket(basket):
    if not basket:
        print("Your basket is empty.")
    else:
        print("\nItems in your basket:")
        total = 0
        for item in basket:
            print(f"- {item['name']}: £{item['price']:.2f}")
            total += item['price']
        print(f"Total: £{total:.2f}\n")

# Main loop
while True:
    print("\nAvailable items:")
    for code, item in items.items():
        print(f"{code}: {item['name']} - £{item['price']:.2f}")

    choice = input("Please enter the ID code of the item that you want to add to your basket. or type 'finish' to complete your order: ")

    if choice == 'finish':
        break
    elif choice in items:
        basket.append(items[choice])
        print(f"{items[choice]['name']} added to your basket.")
    else:
        print("Invalid item ID code. Please enter a valid item ID code.")

# View the final basket
view_basket(basket)
