secret = 37
attempts = 0
won = False

while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret:
        print("Correct! You won.")
        won = True
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

print("Attempts used:", attempts)

if not won:
    print("The secret number was:", secret)