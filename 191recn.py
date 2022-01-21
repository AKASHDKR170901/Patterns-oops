import sys
class customer:
    bankname='DURGABANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('Amount after deposit:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('Insufficient Funds....Cannot perform this operation')
            sys.exit()
        self.balance=self.balance-amt
        print('Amount after withdraw:',self.balance)
print('Welcome to',customer.bankname)
name=input('Enter your name:')
c=customer(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option=input('Enter option:')
    if option=='d' or option=='D':
        amount=eval(input('Enter the amount:'))
        c.deposit(amount)
    elif option=='w' or option=='W':
        amount=eval(input('Enter the amount:'))
        if amount%500 !=0:
            print('Amount should be multiples of 500')
            amount=eval(input('Enter the amount:'))
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thanks for banking....')
        sys.exit()
    else:
        print('Invalid option.....Please choose the correct option....')
    
