
venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
food = float(input("Catering cost: "))
transport = float(input("Transport cost: "))
certificate = float(input("Certificate cost: "))

sponsor = float(input("Sponsorship amount: "))
fee = float(input("Registration fee per student: "))

total = venue + equipment + food + transport + certificate

remaining = total - sponsor

if remaining > 0:
    students = int(remaining / fee) + (remaining % fee > 0)
else:
    students = 0

print("Total Cost:", total)
print("Sponsorship Shortfall:", max(0, remaining))
print("Minimum Registrations:", students)