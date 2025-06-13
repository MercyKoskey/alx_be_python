#bank_account.py
class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance


    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False  # Only return False if withdrawal is invalid


    def display_balance(self):
        print(f"Your account balance is {self.account_balance}")