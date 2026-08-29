while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multication")
    print("4. Division")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "5":
        print("Calculator closed")
        break
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
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