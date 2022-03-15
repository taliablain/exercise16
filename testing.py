from users.customer import Customer
from accounts.bankaccount import BankAccount
from accounts.savings import SavingsAccount
from accounts.studentaccount import StudentAccount
from users.employee import Employee


customer = Customer('talia', 'personal', '8%', '2 years')


employee = Employee('talia', 'finance', 'analyst', 'graduate', '9%')

my_account = BankAccount(5000)
my_account.getbalance()

balance3 = BankAccount(21)
try:
    balance3.withdraw(200)
except Insu:
    balance3.withdraw(21)

savings = SavingsAccount(200)

savings.amount_with_interest(200)

student = StudentAccount(321)
student.available_amount(321)

balance2 = StudentAccount(90)
balance2.deposit(32)
balance2.getbalance()

#next steps, make it so that it can show balance with interest, without needing the
#input 'initial'




balance4 = BankAccount(211)
balance4.balance_in_euros(211)
