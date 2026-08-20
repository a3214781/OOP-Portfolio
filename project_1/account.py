class Account:

    # Attributes
    def __init__(self, number, name, account_type, balance, interest_rate):
        self.__number = number
        self.__account_type = account_type
        self.__name = name
        self.__balance = balance
        self.__interest_rate = interest_rate
        
    def updateAccountInfo(self, new_name, new_account_type):
        self.__name = new_name
        self.__account_type = new_account_type
    
    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            self.__balance = self.__balance + amount
        print("balance = ", self.__balance)

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if self.__balance - amount >= 0:
                self.__balance = self.__balance - amount
                print("balance = ", self.__balance)
            else:
                print("insufficient funds")

    def interest(self):
        if isinstance(int, float):
            self.__balance = self.__balance + (self.__balance * self.__interest_rate)
        print("balance = ", self.__balance)

    def __str__(self):
        return f"Number = {self.__number}, Name = {self.__name}, Type = {self.__account_type}, Account Balance = {self.__balance}"
    # Include the account number, account name, account type, and current balance.

    def __repr__(self):
        return f"Account: number={self.__number}, name={self.__name}, type={self.__account_type}, account_balance={self.__balance}"
    # Include enough attribute values to identify the object’s current state.

    # Behaviors (methods)
        # Withdraw
        # Deposit
        # Intrest"
