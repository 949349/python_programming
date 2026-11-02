budget = float(input("Enter budget in INR: "))
rate = float(input("Exchange rate: "))

expenses = ["Food", "Travel", "Hotel"]
total = 0
largest = ""

for item in expenses:
    amount = float(input(item + " expense: "))
    converted = amount * rate
    total += converted

    if converted > (max_expense if total != converted else 0):
        largest = item
        max_expense = converted

print("Total Expense:", total)
print("Budget:", budget)

if total <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")

print("Largest Expense:", largest)