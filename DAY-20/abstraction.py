#we can't create an object to parent class in abstration
#mandatory to have the abstract methods in the child classes
#abstraction is used to hidden the complexcity to the user, by using the abstract methods
#object can't created to the parent class , only created to the child class

#abstracted the method and rewriting the method


from abc import ABC,abstractmethod 

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")

    @abstractmethod
    def deposit(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass

class SavingAccount(BankAccount):
    def deposit(self):
        print("2 lakhs per day")    
    
    def withdraw(self):
        print("1 lakh you can withdraw")
        
class CurrentAccount(BankAccount):
    def deposit(self):
        print("unlimited deposit")    
    
    def withdraw(self):
        print("unlimited withdraw")

class JointAccount(BankAccount):
    def deposit(self):
        print("only those 2 people can deposit")    
    
    def withdraw(self):
        print("1-2 lakh per day you can withdraw")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("no limit")    
    
    def withdraw(self):
        print("20k - 1L per day")

class PensionAccount(BankAccount):
    def deposit(self):
        print("no deposit")    
    
    def withdraw(self):
        print("40k per day")

print("------------srinidhi-------------")
srinidhi = SavingAccount()
srinidhi.checkbalance()
srinidhi.deposit()
srinidhi.withdraw()

print("------------sangeetha-------------")
sangeetha = CurrentAccount()
sangeetha.checkbalance()
sangeetha.deposit()
sangeetha.withdraw()

print("------------neha-------------")
neha = JointAccount()
neha.checkbalance()
neha.deposit()
neha.withdraw()

print("------------akhil-------------")
akhil = SalaryAccount()
akhil.checkbalance()
akhil.deposit()
akhil.withdraw()

print("------------varsha-------------")
varsha = PensionAccount()
varsha.checkbalance()
varsha.deposit()
varsha.withdraw()




