from person import Person
class Employee(Person):
    #private
    _name = ''

    def __init__(self, name, department, job_role, account_type, interest_rate):
        self._name = name
        self._department = department
        self._job_role = job_role
        self._account_type = account_type
        self._interest_rate = interest_rate

    def display(self):
        print(self._name, self._department, self._job_role, self._account_type, self._interest_rate)