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




#Alex Code

print ("These are the avalible items and prices\n")

#  Item code   Item    Price
#  001         Pizza   £10.00
#  002         Chips   £5.00
#  003         Drink   £2.00

#display list
print ("Code   Product    Price\n")

#directory of availible products, price in pence and number availible
productDictionary = {
  "001":["Pizza", "1000","20"],
  "002":["Chips","500","20"],
  "003":["Drink","200","100"]
}
#print out list of products and price

for x in productDictionary:
  #tempList is copy of list key x
  tempList = productDictionary[x]
  #tempPrice is price of relevant product/100 to display in £
  tempPrice = int(tempList[1])/100
  print(x,"  ", tempList[0],"    £",tempPrice)
print()
#take order
#cart total {quantity, total, running total}
cartTemp={
  "001":["0","0","0"],
  "002":["0","0","0"],
  "003":["0","0","0"]
}
total = 0
runTotal = 0
quantity = 0

for x in productDictionary:
  tempString = productDictionary[x]
  price = int(tempString[1])/100
  maxQuantity = int(tempString[2])
  print ("\nWould you like",tempString[0],"? enter y/n")
  tempAnswer = input()
  if tempAnswer != "y" and tempAnswer != "n":
    print ("ERROR")
    break 
  elif tempAnswer == "y":
    print("How many",tempString[0], "would you like?")
    quantity = int(input())
    if quantity > maxQuantity :
      print ("Sorry we can only supply a maximum of ",maxQuantity)
      quantity = maxQuantity
  total = price * quantity     
  runTotal=runTotal+total
  print (quantity, "x", tempString[0],"= £",total,"     [£",runTotal,"]") 
  cartTemp[x] = [quantity,total,runTotal]


#print order
print ("\nYour order is for :\n")
for x in productDictionary:
  numString = cartTemp[x]
  type = productDictionary[x]
  print (numString[0]," x ", type[0], " =  £",numString[1])
print ("\n      Total  =  £", runTotal)
print ("\n\n\n        Thank you") 
print("\n     Please come again")




#davids code

print ("These are the avalible items and prices\n")

#display list
print ("Code   Product    Price\n")

#directory of availible products, price in pence and number availible
productDictionary = {
  "001":["Pizza","1000","20"],
  "002":["Chips","500","20"],
  "003":["Drink","200","100"]
}
#print out list of products and price



for x in productDictionary:
  #tempList is copy of list key x
  tempList = productDictionary[x]
  #tempPrice is price of relevant product/100 to display in £
  tempPrice = int(tempList[1])/100
  print(x,"  ", tempList[0],"    £",tempPrice)
print()
#take order
order = {}
total = 0

for x in productDictionary:
  tempString = productDictionary[x]
  price = int(tempString[1])/100
  maxQuantity = int(tempString[2])
  print ("\nWould you like",tempString[0],"? enter y/n")
  tempAnswer = input()
  if tempAnswer != "y" and tempAnswer != "n":
    print ("ERROR")
    break 
  elif tempAnswer == "y":
    print("How many",tempString[0], "would you like?")
    quantity = int(input())
    if quantity > maxQuantity :
      print ("Sorry we can only supply a maximum of ",maxQuantity)
      quantity = maxQuantity
    total += price * quantity
    order[x] = quantity 

  # This section asks the user if they want to order the product, prompts for quantity if yes, and handles invalid input.

#print order


print ("\nYour order is for :\n")
# This section iterates through the productDictionary
# If the product code is in the order dictionary it will print the quantity ordered, the product name and the price of the order for that product
for x in productDictionary:
  if x in order:
    type = productDictionary[x]
    print (order[x]," x ", type[0], " =  £",order[x]*int(productDictionary[x][1])/100)
# This section prints the total price of the order
print ("\n      Total  =  £", total)
# This section prints thank you and please come again
print ("\n\n\n        Thank you") 
print("\n     Please come again")
