#2.1 implement a class called  BankAccoumt thar represented a bank account the class should have private attributes for account number,account holder name,and account balanace.Includes method to  deposite money,withdraw money,and display the account balanace.ensure that the account  balanace cannot b uie accessed directly from outside the class.write a program a create an instance of a  BankAccount class and test the deposite  and withdraw all functionalaty 
class BankAccount:
    def __init__(self,  account_number, account_holder_name, initial_balance = 0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance  = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.__account_balance += amount
            print (f"Deposited ₹{amount:.2f} into account           {self.__account_number}")
        else:
            print("Invalid  deposit amount Please deposit a  positive amount.")

    def withdraw(self,amount):
        if amount > 0:
            if self.__account_balance >= amount:
               self. __account_balance -= amount
               print (f"Withdraw $ {account:.2f}from  account {self._account_number}")
            else:
              print("Insufficient balance.Cannot withdraw.")
        else:
           print("Invalid withdraw amount.Please withdraw a positive amount.")

    def display_balance(self):
          print(f"Account {self.__account_number}balance: ${self.__account_balance:.2f}")


# Testing the BankAccount class
if __name__ == "__main__":
  # Create the BankAccount is instance
  account1 = BankAccount(" 123456", "John Doe",1000.0)

  # Deposit money
  account1.deposit(500.0)

  # Withdraw money 
  account1.deposit(200.0)

  # Display balance 
  account1.display_balance()
  

           

    
    
     
                
    