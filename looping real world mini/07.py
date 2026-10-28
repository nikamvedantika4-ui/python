n = int(input("Enter number of employees: "))
total_payroll = 0

for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter basic salary: "))
    hours = float(input("Enter overtime hours: "))

    overtime_pay = hours * 500
    gross = salary + overtime_pay

    if gross >= 50000:
        deduction = gross * 0.05
    else:
        deduction = 0

    net = gross - deduction
    total_payroll += net

    print("Employee:", name)
    print("Gross salary:", gross)
    print("Deduction:", deduction)
    print("Net salary:", net)

print("Total net payroll:", total_payroll)
print("Employee count:", n)