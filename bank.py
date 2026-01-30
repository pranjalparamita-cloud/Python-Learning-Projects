#create a banking system using variables,lst,if_else and while loop.
#features:Deposit,Withdraw,Balance check,Transaction History,Exit
#give 3 attempts to enter correct pin else block the user
#save user name and their pin by user input for authentication dictionary
#initial balance is 10000

balance = 10000
transaction_history = []
print("----------------------Welcome to the Banking System-----------------------------")
user_name = input("Enter your name to create an account: ")
pin = int(input("Set a 4-digit PIN for your account: "))

user_data = {
    user_name: pin
}

attempts = 0

while attempts < 3:
    entered_pin = int(input("Please enter your PIN to access your account: "))
    if entered_pin == user_data[user_name]:
        print("Access granted.")
        print("Which operations u want to perform? \n 1.Deposit \n 2.Withdraw \n 3.Balance Check \n 4.Transaction History \n 5.Exit")
        while True:
            choice=int(input("Enter your choice (1-5): "))
            if choice==1:
                amount=float(input("Enter amount to deposit: "))
                balance += amount
                transaction_history.append(f"Deposited: {amount}")
                print(f"Your {amount} has been deposited successfully.")
                print(f"Your current balance is: {balance}")
            elif choice==2:
                amount=float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    transaction_history.append(f"Withdraw: {amount}")
                    print(f"Your {amount} has been withdrawn successfully.")
                    print(f"Your current balance is: {balance}")
            elif choice==3:
                print(f"Your current balance is: {balance}")
            elif choice==4:
                print("The transaction history is:")
                for i in transaction_history:
                    print(i)
            elif choice==5:
                print("Thank you")
            else:
                print("Invalid choice. Please try again.")
                
                break
    else:
        print("Wrong PIN.") 
        attempts += 1
        if attempts == 3:
            print("Your account has been blocked due to multiple incorrect PIN attempts.")
            