# while True:
#     balance = 1000

#     choice = input(f"Hi Welcome to Umbrella. You have a current balance of {balance}. Would you like to withdraw or deposit? ")


#     if choice.lower() == "deposit":
#         deposit = input("How much would you like to deposit? ")
#         dep = int(deposit)
#         balance = balance + dep
#         print(balance)

#     elif choice.lower() == "withdraw":
#         withdraw = input("How much would you like to withdraw? ")
#         wit = int(withdraw)
#         balance = balance - wit
#         print(balance)
#     else:
#         print("Sorry I did not understand. Try again.")
#     to_exit = input("Would you like to exit? y/n")
#     if to_exit == "y":
#         break

class Bank:
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount
    def log_transaction(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction_string} with a new balance of ${self.balance}\n")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"Withdrew ${amount}")
        
    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"Deposited ${amount}")
account = Bank(5000)
while True:
    try:
        action = input("Hi. Would you like to?")
    except KeyboardInterrupt:
        print("\nLeaving the ATM\n")
        break
    if action in ["withdrawal", "deposit"]:
        if action.lower() == "withdrawal":
            amount = input("How much do you want? ")
            account.withdrawal(amount)
        elif action.lower() == "deposit":
            amount = input("How much would you like to deposit? ")
            account.deposit(amount)

        print(f"Account balance is {self.balance}")
    else:
        print("That is not a valid action. Try again")