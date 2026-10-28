n = int(input("Enter number of students: "))
total = 0
passed = 0
failed = 0

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    while marks < 0 or marks > 100:
        print("Invalid marks. Enter 0 to 100.")
        marks = float(input("Enter marks again: "))

    total += marks

    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    if marks >= 40:
        passed += 1
    else:
        failed += 1

    print(name, "Grade:", grade)

print("Class average:", total / n)
print("Passed:", passed)
print("Failed:", failed)