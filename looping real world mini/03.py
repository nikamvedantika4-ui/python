correct_pin = "1234"
attempts = 0
access = False

while attempts < 3:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("Access Granted")
        access = True
        break
    else:
        print("Incorrect PIN")

print("Attempts used:", attempts)

if not access:
    print("Card Temporarily Locked")