# Real world example of a bank account class to show the benefits of inheritance
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


# Example usage
savings_account = SavingsAccount("SA123", "Alice Smith", 1000, 5)
savings_account.display_balance()  # Output: Account Number: SA123, Balance: 1000
savings_account.deposit(500)  # Output: Deposited 500. New balance: 1500
savings_account.add_interest()  # Output: Interest added: 75.0. New balance: 1575.0
print()  # Just for separation of output
print()  # Just for separation of output
checking_account = CheckingAccount("CA456", "Bob Johnson", 500, 200)
checking_account.display_balance()  # Output: Account Number: CA456, Balance: 500
checking_account.withdraw(600)  # Output: Withdrew 600. New balance: -100
checking_account.display_balance()  # Output: Account Number: CA456, Balance: -100
