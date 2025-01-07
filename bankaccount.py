class bank:
    def __init__(self,accno,name,type):
        self.accno=accno
        self.name=name
        self.type=type
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance : ")
        else:
            self.balance-=amount
    def balance(self):
        print(f"Balance : {self.balance}")
name=input("name : ")
accno=int(input("account no : "))
type=input("account type : ")
account=bank(accno,name,type)
while True:
    choice=int(input("1 deposit 2 withdraw 3 display balance 4 exit : "))
    if choice==1:
        amount=int(input("Deposite amount : "))
        account.deposit(amount)
    elif choice==2:
        amount=int(input("withdraw amount : "))
        account.withdraw(amount)
    elif choice==3:
        account.balance()
    else:
        break