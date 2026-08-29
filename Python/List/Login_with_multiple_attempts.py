# Login system with multiple attempts
# বাস্তব Login System-এ user-এর একাধিক chance থাকে।

correct_password = "Python123"
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        print(f"Wrong password. Attempts left: {attempts}")
if attempts == 0:
    print("Account Blocked")