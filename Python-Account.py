#define classes and functions
class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0, withdraw=0, deposit=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return (self.__id)

    def getBalance(self):
        return (self.__balance)

    def getAnnualInterestRate(self):
        return (self.__annualInterestRate)

    def getMonthlyInterest(self):
        monthlyinterest = self.__balance * (self.__annualInterestRate/1200)
        return (monthlyinterest)

    def setId(self,id2):
        self.__id = id2

    def setBalance(self, balance2):
        self.__balance = balance2

    def setAnnualInterestRate(self, interest2):
        self.__annualInterestRate = interest2

    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        self.__balance -= amount

#call classes and functions
print("Please enter the following information.")
accnum = input("Please enter the last 4 digits of your account number: \n \t")
accbal = 20000
accint = 4.5
accw = eval(input("Please enter the amount you would like to withdraw. \n \t"))
accd = eval(input("Please enter the amount you would like to deposit. \n \t"))
acc1 = Account(accnum, accbal, accint, accw, accd)
acc1.setId(accnum)
acc1.setBalance(accbal)
acc1.setAnnualInterestRate(accint)
acc1.withdraw(accw)
acc1.deposit(accd)
print("The account number ends in", acc1.getId())
print("The balance is $", acc1.getBalance())
print("The annual interest rate is", acc1.getAnnualInterestRate(), "%")
print("The monthly interest is $", acc1.getMonthlyInterest())
