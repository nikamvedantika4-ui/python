num = int(input("Enter a number: "))
original = num
total = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    total += digit ** digits
    num = num // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")