n = int(input("Number of students: "))

students = []

for i in range(n):
    name = input("Name: ")
    marks = int(input("Aggregate marks: "))
    subject = int(input("Minimum subject marks: "))
    attendance = int(input("Attendance: "))
    income = int(input("Family income: "))

    if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
        students.append((name, marks))

students.sort(key=lambda x: x[1], reverse=True)

print("Eligible Students:")
for s in students:
    print(s)