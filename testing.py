from users.customer import Customer
from accounts.bankaccount import BankAccount
from accounts.savings import SavingsAccount
from accounts.studentaccount import StudentAccount

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

balance2 = StudentAccount(90)
balance2.deposit(32)
print(balance2.getbalance())

#next steps, make it so that it can show balance with interest, without needing the
#input 'initial'
#neater formatting and display needed
#tidying up


balance3 = BankAccount(21)
try:
    balance3.withdraw(200)
except:
    balance3.withdraw(21)

balance4 = BankAccount(211)
print(balance4.balance_in_euros(211))
