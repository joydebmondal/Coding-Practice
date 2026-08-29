correct_pin = "1234"
attempts = 3

balance = 100000
withdraw_count = 0
daily_limit = 3
minimum_balance = 5000

while attempts > 0:
    pin = input("Enter PIN: ")
    if pin == correct_pin:

        while withdraw_count < daily_limit:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print("Insufficiant balance")
            elif balance - amount < minimum_balance:
                print("Minimum balance of 5000 must be maintained")
            else:
                balance -= amount
                withdraw_count += 1

                print("Withdrawal successful")
                print(f"Remaining balance: {balance}")
                print(f"Withdrawals today: {withdraw_count}/3")
                break

        if withdraw_count == daily_limit:
            print("You already reached daily withdrawal limit")
            print("You cannot withdraw any more today")
            break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong PIN. Attempts left: {attempts}/3")
            print("please try again")
        
if attempts == 0:
    print("Account Locked")
    print("Please contact your nearest bank brance")