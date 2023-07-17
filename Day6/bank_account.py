#program to deposit or withdraw money in a bank account
class Account:
    def __init__(self):
        self.balance=0
        print("New account created")
    def deposit(self):
        self.deposit_Amount=float(input("enter the amount to deposit"))
        self.balance+=self.deposit_Amount
    def withdraw(self):
        self.withdraw_amount=float(input("enter the amount to withdraw"))
        if(self.balance<self.withdraw_amount):
            print("insufficient balance")
        else:
            self.balance-=self.withdraw_amount
            print("New balance is",self.balance)
    def enquiry(self):
        print("Balance is",self.balance)
a=Account()
a.deposit()
a.withdraw()
a.enquiry()
