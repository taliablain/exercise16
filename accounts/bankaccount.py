#from person import Person


class BankAccount:
    numCreated = 0
    def __init__(self, initial):
        self._balance = initial
        BankAccount.numCreated += 1

    def deposit(self, amount):
        self._balance += amount
        print(f'available funds: £{self._balance}')
        return

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFunds
        self._balance -= amount
        print(f'remaining funds: £{self._balance}')


    def getbalance(self):
        print(f'available funds: £{self._balance}')
        return self._balance

    def balance_in_euros(self, initial):
        self._balance = initial * 1.19
        print(f'balance in euros: €{self._balance}')
        return self._balance