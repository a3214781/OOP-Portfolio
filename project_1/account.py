class Account:
    
    # Attributes
    def __init__(self, number, account_type, balance, interest_rate):
        self.number = number
        self.account_type = account_type
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("balance = ", self.balance)
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("balance = ", self.balance)
        else:
            print("insufficient funds")
            
    def interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate)
        print("balance = ", self.balance)
    
    # Behaviors (methods)
        # Withdraw
        # Deposit
        # Intrest