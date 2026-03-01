# Another example of method overriding in Python
class PaymentMethod:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using a generic payment method.")


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using Credit Card ending in {self.card_number[-4:]}")


class DebitCardPayment(PaymentMethod):
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin

    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using Debit Card ending in {self.card_number[-4:]} with PIN verification")


class DigitalWalletPayment(PaymentMethod):
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using Digital Wallet with ID {self.wallet_id}")


# Creating objects of different payment methods
credit_card = CreditCardPayment("1234-5678-9012-3456")
debit_card = DebitCardPayment("9876-5432-1098-7654", "1234")
digital_wallet = DigitalWalletPayment("wallet_001")

# Processing payments using different payment methods
credit_card.process_payment(100)  # Output: Processing payment of $100 using Credit Card ending in 3456
print()
debit_card.process_payment(50)  # Output: Processing payment of $50 using Debit Card ending in 7654 with PIN verification
print()
digital_wallet.process_payment(75)  # Output: Processing payment of $75 using Digital Wallet with ID wallet_001
