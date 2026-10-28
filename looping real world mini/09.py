balance = float(input("Enter opening balance: "))
n = int(input("Enter number of transactions: "))

deposits = 0
successful_withdrawals = 0
rejected_withdrawals = 0

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdrawal")
    choice = int(input("Enter transaction type: "))
    amount = float(input("Enter amount: "))

    if choice == 1:
        balance += amount
        deposits += 1
        print("Deposit successful")

    elif choice == 2:
        if amount <= balance:
            balance -= amount
            successful_withdrawals += 1
            print("Withdrawal successful")
        else:
            rejected_withdrawals += 1
            print("Insufficient balance")

    else:
        print("Invalid transaction type")

print("\n--- Bank Transaction Summary ---")
print("Final Balance: ₹", balance)
print("Total Deposits:", deposits)
print("Successful Withdrawals:", successful_withdrawals)
print("Rejected Withdrawals:", rejected_withdrawals)

if balance < 1000:
    print("Warning: Balance is below ₹1000")