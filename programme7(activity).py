n = int(input("Number of products: "))
total = 0

for i in range(n):
    price = float(input("Product price: "))
    quantity = int(input("Quantity: "))
    total += price * quantity

if total >= 5000:
    discount = total * 0.10
else:
    discount = total * 0.05

tax = total * 0.05
final = total - discount + tax

print("Total:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", final)