#from person import Person

class BankAccount:
    numCreated = 0
    def __init__(self, initial):
        self._balance = initial
        BankAccount.numCreated += 1

    def deposit(self, amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        self._balance -= amount
        return

    def getbalance(self):
        return self._balance