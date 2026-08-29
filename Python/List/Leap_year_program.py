# Rule:
# 400 দিয়ে divisible → Leap Year
# অথবা 4 দিয়ে divisible কিন্তু 100 দিয়ে নয় → Leap Year

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not Leap Year")