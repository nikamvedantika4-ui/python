days = int(input("Enter number of days: "))
total = 0
highest = 0
high_days = 0

for i in range(1, days + 1):
    units = float(input("Enter units used today: "))
    total += units

    if i == 1 or units > highest:
        highest = units

    if units > 10:
        high_days += 1

average = total / days

print("Total units:", total)
print("Average usage:", average)
print("Days above 10 units:", high_days)
print("Maximum daily usage:", highest)

if total > 300:
    print("High Usage")
else:
    print("Normal Usage")