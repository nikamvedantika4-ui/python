sidea=int(input("enter the value of a:"))
sideb=int(input("enter the value of b:"))
sidec=int(input("enter the value of c:"))
if sidea==sideb==sidec:
    print("the triangle is equilateral")
elif sidea==sideb or sideb==sidec or sidec==sidea:
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")
