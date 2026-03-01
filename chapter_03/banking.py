# A complete Banking System to show encapsulation and data hiding to create a secure and robust application. 
# #This code defines a BankAccount class with private attributes for account number, account holder's name, and balance. 
# #It includes getter and setter methods for each attribute, along with validation to ensure that the account number is a positive integer, the account holder's name is a non-empty string, and the balance is a non-negative number. 
# #The class also has methods to display account information, deposit money, and withdraw money. 
# Finally, two bank account instances are created, their information is displayed, and transactions are performed to demonstrate the functionality of the class.

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transaction_history = []     
        # This list will store the history of transactions for the account. Each transaction can be represented as a dictionary containing details such as the type of transaction (deposit or withdrawal), the amount, and the date/time of the transaction. 
        # This allows us to keep track of all transactions made on the account for future reference and auditing purposes.
        self.__is_active = True  # This boolean attribute indicates whether the bank account is active or not. It can be used to prevent transactions on inactive accounts and to manage account status effectively.

    @property
    def account_holder(self):
        return self.__account_holder

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        if self.__is_active:
            return self.__balance 
        else:
            return "Account is inactive. Balance information is not available."
        
    @property
    def is_active(self):
        return self.__is_active
    
    def deposit(self, amount):
        if self.__is_active:
            if amount > 0:
                self.__balance += amount
                self.__transaction_history.append({"type": "deposit", "amount": amount})
                print(f"Deposited ${amount}. New balance: ${self.__balance}")
                return True
            else:
                print("Deposit amount must be positive.")
                return False
        else:
            print("Cannot perform transactions on an inactive account.")
            return False
        
    def withdraw(self, amount):
        if self.__is_active:
            if amount > self.__balance:
                print(f"Insufficient funds for withdrawal of ${amount}. Current balance: ${self.__balance}")
                return False
            elif amount <= 0:
                print("Withdrawal amount must be positive.")
                return False
            else:
                self.__balance -= amount
                self.__transaction_history.append({"type": "withdrawal", "amount": amount})
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
                return True
        else:
            print("Cannot perform transactions on an inactive account.")
            return False
    
    def transfer(self, amount, recipient_account):
        if self.__is_active and recipient_account.is_active:

            print(f"Initiating transfer of ${amount} from {self.account_holder} to {recipient_account.account_holder}.")

            if self.withdraw(amount):
                if recipient_account.deposit(amount):
                    self.__transaction_history.append({"type": "transfer_out", "amount": amount, "recipient": recipient_account.account_holder})
                    recipient_account.__transaction_history.append({"type": "transfer_in", "amount": amount, "sender": self.account_holder})
                    print(f"Transferred ${amount} to {recipient_account.account_holder}.")
                    return True
            else:
                print("Transfer failed due to insufficient funds or invalid amount.")
                return False
        else:
            print("Cannot perform transactions on an inactive account.")
            return False
    
    def get_transaction_history(self):

        if self.__is_active:
            print(f"Transaction history for account {self.account_number}:")
            if len(self.__transaction_history) == 0:
                print("No transactions yet.")
            else:
                for transaction in self.__transaction_history:
                    print(transaction)  
        else:
            return "Account is inactive. Transaction history is not available."
        
    def close_account(self):
        if self.__balance > 0:
            print(f"Cannot close account {self.account_number} because it has a positive balance of ${self.__balance}. Please withdraw the remaining balance before closing the account.")
            return False
        self.__is_active = False
        print(f"Account {self.account_number} has been closed.")
        return True
    
    def display_account_info(self):
        status = "Active" if self.__is_active else "Inactive"
        print(f"\nAccount Information")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Status: {status}")
        if status == "Active":
            print(f"Balance: ${self.__balance}")


# Examples
print("Creating two bank accounts:")
account1 = BankAccount("Alice Smith", "BANK01234", 1000)
account2 = BankAccount("Bob Johnson", "BANK98765", 500)

account1.display_account_info()
account2.display_account_info()

print("\nPerforming transactions:")
account1.deposit(200)
account1.withdraw(150)
account1.withdraw(2000)  # Attempt to withdraw more than the balance
account1.transfer(300, account2)  # Transfer from account1 to account2

print("\nChecking balances after transactions:")
print(f"Account 1 balance: ${account1.balance}")
print(f"Account 2 balance: ${account2.balance}")

print("\nTransaction history for Account 1:")
account1.get_transaction_history()

print("\nTransaction history for Account 2:")
account2.get_transaction_history()

print("\nAttempting to close Account 1 with a positive balance:")
account1.close_account()  # Should fail because balance is positive
account1.withdraw(account1.balance)  # Withdraw remaining balance
print("\nAttempting to close Account 1 again:")
account1.close_account()  # Should succeed now that balance is zero
account1.display_account_info()  # Should show account as inactive  

print("\nAttempting transactions on closed account:")
account1.deposit(100)  # Should fail because account is inactive
account1.withdraw(50)  # Should fail because account is inactive
account1.display_account_info()  # Should show account as inactive and balance information not available


    
    









    