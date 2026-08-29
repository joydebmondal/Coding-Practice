# import keyword
# print(keyword.kwlist)
# import types
# print(dir(types))

# x = int("100")
# print(x)
# print(type(x))

# a = "200"
# b = int(a)
# print(b)
# print(type(b))
# print(type(a))

# Create variables:
# name = "Joydeb"
# age = 25
# country = "India"
# print("My name is", name)
# print("I am", age, "years old.")
# print("I live in", country)

# Take two numbers from user and print:
# Addition
# Subtraction
# Multiplication
# Division

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print("Addition = ", a + b)
# print("Subtraction = ", a - b)
# print("Multiplication = ", a * b)
# print("Division = ", a / b)

# Convert:
# "500"
# into integer and add 100.

# a = "500"
# b = 100
# c = int(a)
# print(c + b)

# a = int("500")
# b = 100
# print(a + b)

# Find the type of:
# 10
# 10.5
# "Python"
# True
# None

# a = 10
# b = 10.5
# c = "python"
# d = True
# e = None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print(type(10))
# print(type(10.5))
# print(type("Python"))
# print(type(True))
# print(type(None))

# language = "python"
# for ch in language:
#     print(ch)

# "Bangladesh" String-এর প্রথম ও শেষ Character প্রিন্ট করো।
# country = "Bangladesh"
# print(country[0])
# print(country[-1])

# "Programming"-এর Length বের করো।
# name = "Programming"
# print(len(name))

# "Python"-এর প্রতিটি Character আলাদা লাইনে প্রিন্ট করো।
# sub = "Python"
# # for ch in sub:
# #     print(ch)

# for i in range(len(sub)):
#     print(sub[i])

# "OpenAI"-এর Negative Index ব্যবহার করে শেষ ৩টি Character প্রিন্ট করো।
# source = "OpenAI"
# print(source[-3:])

# "Hello" String-কে "Jello" করার চেষ্টা করো এবং কেন Error আসে তা ব্যাখ্যা করো।
# name = "Hello"
# name[0] = "J" # TypeError, Because python does not change string character or string. python create new string.
# name = "Jello"
# print(name)

# Email Username বের করা
# email = "joy123@gmail.com"
# print(email[:3])

# File Extension
# image = "photo.jpg"
# print(image[-3:])

# Mobile Number শেষ ৪ Digit
# mobile = "9332985974"
# print(mobile[-4:])

# First Name
# name = "Joydeb Mondal"
# print(name[:6])

# Question 1: Convert python into PYTHON
# text = "python"
# print(text.upper())

# Question 2: Replace Java with Python
# text = "I love Java"
# print(text.replace("Java", "Python"))

# Question 3: Count 'a' in Banana 
# text = "Banana"
# print(text.count("a"))

# Question 4: Split Apple,Mango,Banana 
# text = "Apple,Mango,Banana"
# print(text.split(","))

# Question 5: Join ["A","B","C"] using -
# text = ["A","B","C"]
# print("-".join(text))

# Problem 1: User-এর Age Input নিয়ে বলো Eligible or Not Eligible
# Age = int(input("Enter your age: "))
# if Age >= 18:
#     if Age <= 59:
#         print("Eligible")
#     else:
#         print("Not Eligible")

# Problem 2: দুইটি Number-এর মধ্যে বড়টি Print করো।
# a = 120
# b = 2315
# if a > b:
#     print(a)
# else:
#     print(b)

# Problem 3: Marks Input নিয়ে Grade Print করো।
# marks = int(input("Enter Marks: "))
# if marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# elif marks >= 70:
#     print("B")
# elif marks >= 60:
#     print("C")
# elif marks >= 50:
#     print("D")
# else:
#     print("Fail")

# Problem 4: Number Positive / Negative / Zero Check করো।
# number = int(input("Enter Number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# Problem 5: Password Check Program লিখো।
# password = input("Enter password: ")
# if password == "python123":
#     print("Access Granted")
# else:
#     print("Wrong Password")

# marks = 82
# grade = ("A+" if marks >= 90 else "A" if marks >= 80 else "B" if marks >= 70 else "Fail")
# print(grade)


# Problem 1: User-এর Username এবং Password Input নিয়ে Login Check করো।
# Username = "Joydeb Mondal"
# Password = "25800"
# username = input("Enter Your Username: ")
# password = input("Enter Password: ")
# if username == Username and password == Password:
#     print("Login successful")
# else:
#     print("Wrong username or password")


# Problem 2: তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করো।
# num1 = int(input("Enter 1st Number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# if num1 > num2:
#     print(num1)
# elif num2 > num3:
#     print(num2)
# else:
#     print(num3)

# Problem 3: Leap Year Check করো।
# Hint:
# 400 দিয়ে বিভাজ্য → Leap Year
# অথবা 4 দিয়ে বিভাজ্য কিন্তু 100 দিয়ে নয় → Leap Year
# year = int(input("Enter year: "))
# if year % 400 == 0:
#     print("Leap Year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# Problem 4: # Calculator বানাও।
# Operations:
# . +
# . -
# . *
# . /
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# operator = input("Enter operator (+, -, *, /): ")
# if operator == "+":
#     print("Result: ", num1 + num2)
# elif operator == "-":
#     print("Result: ", num1 - num2)
# elif operator == "*":
#     print("Result: ", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Result: ", num1 / num2)
#     else:
#         print("Cannot divide by zero ")
# else:
#     print("Invalid operator")

# Problem 5: User-এর Age এবং Citizen Status নিয়ে Vote Eligibility Check করো।
# age = int(input("Enter your age: "))
# citizen = True
# if age >= 18 and citizen:
#     print("Eligible for vote")
# else:
#     print("Not Eligible for vote")

while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "5":
        print("Calculator closed")
        break

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if choice == "1":
        print(a + b)

    elif choice == "2":
        print(a - b)

    elif choice == "3":
        print(a * b)

    elif choice == "4":
        if b != 0:
            print(a / b)
        else:
            print("Division by zero not allowed")

    else:
        print("Invalid choice")