#odd or even
num = int(input("Enter your number: "))
rem = num % 2
if(rem == 0):
    print("EVEN")
else:
    print("ODD")

# which one large number 
a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))
c = int(input("Enter your 3rd number: "))
if(a >= b and a >= c):
    print(a, "is largest number.")
elif(b >= c):
    print(b, "is largest number.")
else:
    print(c, "is largest number.")


num = int(input("Enter your number: "))
rem = num % 7
if(rem == 0):
    print(num, "This number is multiple of 7")
else:
    print(num, "This number is not multiple of 7")