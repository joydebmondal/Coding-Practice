# User-এর age নিয়ে vote eligibility check।
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligibile for vote")
# else:
#     print("Not Eligibile for vote")

# Number even/odd।
# number = int(input("Enter number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Positive/negative/zero।
# number = int(input("Enter number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:    
#     print("Zero")

# Password check।
# login_id = "Admin"
# correct_password = "admin@123"
# attempts_count = 0
# attempts = 3
# while attempts_count < attempts:
#     username = input("Enter Username: ")
#     password = input("Enter password: ")
#     if username == login_id and password == correct_password:
#         print("Login Successful")
#         break
#     else:
#         attempts_count += 1
#         print("Incorrect  Username or Password")
#         print(f"Attempts left: {attempts - attempts_count}")
# else:
#     print("Acount Blocked")


# Largest of two numbers।
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# if a > b:
#     print(f"Largest number: {a}")
# elif b > a:
#     print(f"Largest number: {b}")
# else:
#     print("Both number are Equal")


# Largest of three numbers।
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))
# if a > b and a > c:
#     print(a, "is largest number")
# elif b > a and b > c:
#     print(b, "is largest number")
# else:
#     print(c, "is largest number")


# Leap year।
# year = int(input("Enter Year: "))
# if year % 400 == 0:
#     print("Leap Year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# Grade system।
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("A-")
# elif marks >= 60:
#     print("B")
# elif marks >= 50:
#     print("C")
# elif marks >= 33:
#     print("D")
# else:
#     print("Fail")


# Calculator।
# a = float(input("Enter 1st number: "))
# op = input("Operator (+, -, *, /): ")
# b = float(input("Enter 2nd number: "))
# if op == "+":
#     print(a+b)
# elif op == "-":
#     print(a-b)
# elif op == "*":
#     print(a*b)
# elif op == "/":
#     if b != 0:
#         print(a/b)
#     else:
#         print("Cannot devide by zero")
# else:
#     print("Invalid Operator")


# ATM withdrawal।
# correct_pin = "1234"
# attempts = 3
# balance = 100000
# withdrawals_count = 0
# daliy_limit = 3
# minimum_balance = 5000
# while attempts > 0:
#     pin = input("Enter PIN: ")
#     if pin == correct_pin:
#         while withdrawals_count < daliy_limit:
#             amount = int(input("Enter amount: "))
#             if amount <= 0:
#                 print("Invalid amounrt")
#             elif amount > balance:
#                 print("Insufficient Balance")
#             elif balance - amount < minimum_balance:
#                 print("Minimum balance of 5000 must be maintained")
#             else:
#                 balance -= amount
#                 withdrawals_count += 1
#                 print("Withdrawals Successful")
#                 print(f"Remaining Balance: {balance}")
#                 print(f"Withdrawals Today: {withdrawals_count}/3")
#                 break
#         if withdrawals_count == daliy_limit:
#             print("You reached daliy withdrawal limit. \nYou cannot withdraw any more today.")
#             break
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(f"Wrong PIN. Attempts left: {attempts}/3")
#             print("Please try again")            
# if attempts == 0:
#     print("Acount Locked")
#     print("Please contact with nearest bank brance")       



# Login with 3 attempts।
# user_id = "Admin"
# correct_password = "admin@123"
# attempts = 3
# while attempts > 0:
#     username = input("Enter Username: ")
#     password = input("Enter password: ")
#     if username == user_id and password == correct_password:
#         print("Login Successful")
#         break
#     else:
#         attempts -= 1
#         print("Incorrect username or password. Please try again.")
#         print(f"Attempts Left: {attempts}")
# if attempts == 0:
#     print("Acount Locked")

# Electricity bill calculation।
# units = int(input("Enter Units: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = 100 * 5 + (units - 100) * 7
# else:
#     bill = 100 * 5 + 100 * 7 + (units - 200) * 10
# print("Bill: ", bill)


# Income tax calculation।
# income = float(input("Enter anual income: "))
# if income <= 300000:
#     tax = 0
# elif income <= 600000:
#     tax = (income - 300000) * 0.05
# elif income <= 900000:
#     tax = 300000 * 0.05 + (income - 600000) * 0.10
# else:
#     tax = 300000 * 0.05 + 300000 * 0.10 + (income - 900000) * 0.20
# print("Tax: ", tax)

# BMI category।
# weight = float(input("Weight (kg): "))
# height = float(input("Height (m): "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")


# Triangle validity check।
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")

# Triangle type (equilateral, isosceles, scalene)।
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print("Equilateral")
# elif a == b or a == c or b == c:
#     print("Isosceles")
# else:
#     print("Scalene")


# Character vowel/consonant।
# ch = input("Enter a Character: ").lower()
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


# Character alphabet/digit/special।
# ch = input("Enter a Character: ")
# if ch.isalpha():
#     print("Alphabet")
# elif ch.isdigit():
#     print("Digit")
# else:
#     print("Special Character")

# Number palindrome check।
# num = input("Enter a Number: ")
# if num == num[::-1]:
#     print("Number is Palindrome")
# else:
#     print("Not Palindrome")

# Simple menu-driven application।
# while True:
#     print("\n1. Even/Odd")
#     print("2. Largest of Two")
#     print("3. Exit")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         n = int(input("Enter number: "))
#         if n % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#     elif choice == "2":
#         a = int(input("A: "))
#         b = int(input("B: "))
#         if a > b:
#             print(a)
#         else:
#             print(b)
#     elif choice == "3":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice")