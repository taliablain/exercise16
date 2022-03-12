from customer import Customer
from employee import Employee
from bankaccount import BankAccount
from savings import SavingsAccount
from currentaccount import CurrentAccount
from studentaccount import StudentAccount

customer = Customer('talia', 'personal', '8%', '2 years')
##print(customer.display())

#employee = Employee('talia', 'finance', 'analyst', 'graduate', '9%')

balance = BankAccount(5000)
balance.deposit(32)
#print(balance.getbalance())
savings = SavingsAccount(200)

print(savings.amount_with_interest(200))

student = StudentAccount(321)
print(student.available_amount(321))
