from accounts.bankaccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, initial):
        self._balance = initial

    def amount_with_interest(self, initial):
        self._balance = int(initial * 1.006)
        print(f'balance with interest: £{self._balance}')
        return self._balance





