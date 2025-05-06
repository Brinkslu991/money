# Lucas Brinks
# 5/6/25
# Three Ways to Modify BankAccount Class Attributes

class BankAccount:
    def __init__(self,account_holder,balence = 0):
        self.account_holder = account_holder
        self.balence = balence
    def diposit(self, amount):
        if amount > 0:
            self.balence += amount
            print(f'amount was added, your new balence is {self.balence}')
        else:
            print(f'Invaled deposit amount')
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balence:
            self.balence -= amount
            print(f'Money withdrawn {amount}, new balence: {self.balence}')
        else:
            print(f'Invalid withdrawal amount or insufficient funds')
    def get_balence(self):
        return self.balence
    def display_account_info(self):
        print(f'The owner of this account is {self.account_holder} and your balence is {self.balence}')

my_bank = BankAccount('Lucas', 1500)


my_bank.display_account_info()
my_bank.diposit(1500)
my_bank.display_account_info()
my_bank.withdraw(200)
my_bank.display_account_info()
my_bank.withdraw(-499)
