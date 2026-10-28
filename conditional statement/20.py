age=int(input("enter your age:"))
if age<18:
    print("ticket price is 50")
elif age>=18 and age<60:
    print("ticket price is 100")
else:
    print("ticket price is 150")