material = float(input("Material cost: "))
labour = float(input("Labour cost: "))
machine = float(input("Machine cost: "))
wastage = float(input("Wastage cost: "))
selling = float(input("Selling price: "))

cost = material + labour + machine + wastage
profit = selling - cost

print("Total Cost:", cost)
print("Profit:", profit)

if profit >= 1000:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")