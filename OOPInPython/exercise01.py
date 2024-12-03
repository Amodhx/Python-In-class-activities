# create a class named BankAccount with the following 
# an attribute account_holder to store the name of the account holder
# an attribute balance to store the account balance , initialize to 0 

# Add the following methods to the class 
#   Deposit - add the given amount to the balance
#   withdrow - sub the given amount from the balance 
#  if sufficent funds exits ,  othervise print an error messege
#   Display balance 


# write the samll script to demostarte the following 
#   Create an obj of the bank account class 
#   perform a few deposite and withdrawal operation
#   display the balance afrte edit operations

class BankAccount:
    def __init__(self,holder):
        self.account_holder = holder
        self.amount = 0
    
    def deposit_funds(self,amount):
        if amount > 0:
            self.amount += amount
    
    def withraw_funds(self,amount):
        if self.amount > amount :
            self.amount -= amount
        else :
            print("Cant get this amount!!")
    
    # def fund_manager(self,operation,amount):
    #     if operation == "add":
    #         self.amount += amount
    #     else : 
    #         self.amount -= amount
        
    def display_amount(self):
        print(self.account_holder , " balance is : ", self.amount)



my_account = BankAccount("Amodh")

my_account.deposit_funds(5000)
my_account.deposit_funds(4000)
my_account.display_amount()

my_account.withraw_funds(1000)
my_account.display_amount()

my_account.withraw_funds(9000)
my_account.display_amount()