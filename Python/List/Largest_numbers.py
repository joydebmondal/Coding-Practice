a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd number: "))

if a >= b and a >= c:
    print("a")
elif b >= a and b >= c:
    print("b")
else:
    print("c")