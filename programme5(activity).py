usage = int(input("Enter data usage in GB: "))

plans = {
    "Plan A": (199, 10, 10),
    "Plan B": (299, 20, 5),
    "Plan C": (399, 30, 0)
}

costs = {}

for name, (price, limit, extra) in plans.items():
    cost = price + max(0, usage - limit) * extra
    costs[name] = cost

best = min(costs, key=costs.get)

print("Plan Costs:", costs)
print("Best Plan:", best)
print("Minimum Cost:", costs[best])