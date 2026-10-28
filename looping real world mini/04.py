n = int(input("Enter number of products: "))
subtotal = 0

for i in range(1, n + 1):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    while price < 0 or quantity < 0:
        print("Negative values are not allowed")
        price = float(input("Enter price again: "))
        quantity = int(input("Enter quantity again: "))

    subtotal += price * quantity

if subtotal >= 3000:
    discount = subtotal * 0.10
else:
    discount = 0

amount = subtotal - discount

if amount < 1500:
    delivery = 100
else:
    delivery = 0

final_amount = amount + delivery

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Delivery charge:", delivery)
print("Final payable amount:", final_amount)