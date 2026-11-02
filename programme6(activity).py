distance = int(input("Enter distance: "))
age = int(input("Enter age: "))
choice = input("Class (Sleeper/AC): ")

rate = 2 if choice == "Sleeper" else 5
fare = distance * rate

if age >= 60:
    fare *= 0.8

fare += 30

print("Railway Fare:", fare)