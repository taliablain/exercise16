from person import Person
class Customer(Person):
    #private
    _name = ''

    def __init__(self, name, account_type, interest_rate, customer_history):
        self._name = name
        self._account_type = account_type
        self._interest_rate = interest_rate

    def display(self):
        print(self._name, self._account_type, self._interest_rate)


