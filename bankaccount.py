#from person import Person
class InsufficientFunds(Exception):
    print('Insufficient funds in account')
    pass



class BankAccount:
    numCreated = 0
    def __init__(self, initial):
        self._balance = initial
        BankAccount.numCreated += 1

    def deposit(self, amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFunds
            self._balance -= amount
        return

    def getbalance(self):
        return self._balance