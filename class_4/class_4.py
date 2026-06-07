from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CardPayment(Payment):
    def pay(self):
        return "Payment completed using card"

txn = CardPayment()
print(txn.pay())        
