consultation = int(input("Consultation charge: "))
diagnostic = int(input("Diagnostic charge: "))
treatment = int(input("Treatment charge: "))

total = consultation + diagnostic + treatment

if total >= 10000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

if final_bill >= 10000:
    category = "High Payment"
else:
    category = "Normal Payment"

print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
print("Patient Category:", category)