basic = float(input("Basic salary: "))
allowance = float(input("Allowances: "))
overtime = float(input("Overtime pay: "))
incentive = float(input("Incentive: "))

gross = basic + allowance + overtime + incentive

if gross <= 20000:
    tax = gross * 0.05
else:
    tax = gross * 0.10

net = gross - tax

print("Gross Salary:", gross)
print("Deduction:", tax)
print("Net Salary:", net)