# ধরো একটি website-এর password policy হলো:
# কমপক্ষে 8 characters
# অন্তত 1টি uppercase letter
# অন্তত 1টি lowercase letter
# অন্তত 1টি digit

password = input("Enter Password: ")
has_upper = False
has_lower = False
has_digit = False
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Strong Password")
else:
    print("Week Password")