year=int(input("enter a year"))
if year%100==0:
    if year%400==0:
        print("the year is century and leap year")
    else:
        print("the year is century but not a leap year")
else:
    print("the year is not a leap year nor a century year")