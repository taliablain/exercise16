from bankaccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, initial):
        self._balance = initial

    def amount_with_interest(self, initial):
        self._balance = int(initial * 0)
        return  self._balance
