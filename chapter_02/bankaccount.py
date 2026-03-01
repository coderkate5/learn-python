class Bankaccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number} has a balance of: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Your account does not have sufficient funds for a withdrawal of ${amount}. Current balance: ${self.balance} ")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


main_account = Bankaccount("Sarah Jones", "123456789", 1000)
secundary_account = Bankaccount("John Smith", "987654321", 5050)

main_account.display_info()
main_account.deposit(500)
main_account.withdraw(200)
main_account.withdraw(2000)
main_account.check_balance()

secundary_account.display_info()
secundary_account.deposit(50)
secundary_account.withdraw(100)
secundary_account.withdraw(6000)
secundary_account.check_balance()
