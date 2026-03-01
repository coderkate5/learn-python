# Payment processing system using abstraction 
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, transaction_id):
        pass

    def display_confirmation(self):
        print(f"Payment processed successfully.")


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}.")
        return f"Transaction ID: CC{amount}001"

    def refund_payment(self, transaction_id):
        print(f"Refunding credit card payment with transaction ID: {transaction_id}.")


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}.")
        return f"Transaction ID: PP{amount}001"

    def refund_payment(self, transaction_id):
        print(f"Refunding PayPal payment with transaction ID: {transaction_id}.")

# Using the payment processors
credit_card_processor = CreditCardProcessor()
transaction = credit_card_processor.process_payment(100)
credit_card_processor.display_confirmation()
credit_card_processor.refund_payment(transaction)

print()

paypal_processor = PayPalProcessor()
transaction = paypal_processor.process_payment(50)
paypal_processor.display_confirmation()
paypal_processor.refund_payment(transaction)
