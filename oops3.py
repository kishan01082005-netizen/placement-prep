class Atm:
    def __init__(self, balance=0):
        self.balance = balance
        self.__pin = None

    def check_balance(self):
        return f"Your current balance is: ${self.balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: ${amount}. New balance: ${self.__balance}"
        return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: ${amount}. New balance: ${self.__balance}"

    
    
acc=Atm(1000)
print(acc.balance)
