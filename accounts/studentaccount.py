from accounts.bankaccount import BankAccount

class StudentAccount(BankAccount):
    def __init__(self, initial):
        self._balance = initial

    def available_amount(self, initial):
        self._balance = int(initial + 1000)
        return  self._balance