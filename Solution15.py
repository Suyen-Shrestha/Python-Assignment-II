
class BankAccount:

    def __init__(self):
        self.balance = 0


    def deposit_amount(self):
        amount = float(input('Enter the amount you want to deposit: '))
        self.balance += amount
        print(f'Amount Rs.{amount} deposited successfully!!')


    def withdraw_amount(self):
        amount = float(input('Enter the amount you want to withdraw: '))
        if self.balance >= amount:
            self.balance -= amount
            print(f'Amount Rs.{amount} withdrawn successfully!!')
        else:
            print(f'Insufficient Balance!!')

    def fetch_balance(self):
        print(f'Your Current Total Balance: Rs.{self.balance} ')       


print('Welcome to a sample banking app!\n')

she = BankAccount()

she.deposit_amount()
she.withdraw_amount()
she.fetch_balance()

