class Bankaccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance # The balance is a protected member, indicated by the single underscore prefix. It is intended to be accessed and modified only within the class and its subclasses, but it can still be accessed from outside the class if needed.

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Your account does not have sufficient funds for a withdrawal of ${amount}. Current balance: ${self._balance} ")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")

    def get_balance(self):
        return self._balance


main_account = Bankaccount("BANK0123456789", 2599)
secundary_account = Bankaccount("BANK0987654321", 1023)

# Examples of protected member access
main_account.deposit(500)
main_account.withdraw(200)
main_account.withdraw(2000)
print(f"Balance through method: ${main_account.get_balance()}")
print(f"Direct access to protected member: ${main_account._balance}")


secundary_account.deposit(50)
secundary_account.withdraw(100)
secundary_account.withdraw(6000)
print(f"Balance through method: ${secundary_account.get_balance()}")
print(f"Direct access to protected member: ${secundary_account._balance}")
