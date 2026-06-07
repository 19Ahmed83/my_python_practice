class Account:
    def __init__(self, username, balance):
        self.username = username
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        self.__balance = amount

acc = Account("alex", 5000) 
print(acc.get_balance())
acc.update_balance(7000)
print(acc.get_balance())           