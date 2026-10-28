days = int(input("Enter number of days: "))
total = 0
highest = 0

for i in range(1, days + 1):
    expense = float(input("Enter expense for day " + str(i) + ": "))

    total += expense

    if i == 1 or expense > highest:
        highest = expense

average = total / days

print("Total expense:", total)
print("Average daily expense:", average)
print("Highest daily expense:", highest)

if total > 5000:
    print("Budget Alert")
else:
    print("Within Budget")