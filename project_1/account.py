class Account:
    """The Account class is responsible for representing a Account 
    of the client through (number, name, account_type, balance, 
    interest_rate).

    Account does not manage who it belongs to,that responsibility belongs 
    to the Client class though addAccount()."""

    def __init__(self, number, name, account_type, balance, interest_rate):
        # number must be a positive int and not a boolean which come up as 1 and 0
        if isinstance(number, int) and not isinstance(number, bool) and number > 0:
            self.__number = number
        else:
            self.__number = 0
            print("Account number is invalid.")

        # name must be a valid string or no name will be applied to the account
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = "No Name"
            print("Name is invalid.")

        # account_type must be a string of no type will be applied to teh account
        if isinstance(account_type, str):
            self.__account_type = account_type
        else:
            self.__account_type = "No Type"
            print("Account type is invalid.")

        # balance must be a positive number and not a bool to represent total balance of the account
        if isinstance(balance, (int, float)) and not isinstance(balance, bool) and balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0
            print("Balance is invalid.")

        # interest_rate must be a positive number and not a bool as interest cannot loose money.
        if isinstance(interest_rate, (int, float)) and not isinstance(interest_rate, bool) and interest_rate >= 0:
            self.__interest_rate = interest_rate
        else:
            self.__interest_rate = 0
            print("Interest rate is invalid.")

    # Getters: This is used to get private variables from the constructor without calling them
    def get_number(self):
        return self.__number

    def get_name(self):
        return self.__name

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    def get_interest_rate(self):
        return self.__interest_rate

    # Setter: Used to set attributes similarly to the constructor, so you are able to reenter values.
    #
    # update_account_info: name and account_type change together, validated the same as the constructor so that there are no type errors.
    def update_account_info(self, new_name, new_account_type):
        if isinstance(new_name, str) and isinstance(new_account_type, str):
            self.__name = new_name
            self.__account_type = new_account_type
            print("Account info updated")
        else:
            print("Invalid account info. Nothing changed.")

    # deposit (+): balance only ever increases through deposit(), it cannot be set directly through this function
    def deposit(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            self.__balance = self.__balance + amount
            print("balance = ", self.__balance)
        else:
            print("Invalid deposit amount.")

    # withdraw (-): balance decreases through withdraw(), although never below zero as that would mean you withdraw more money then you have in your account
    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            if self.__balance - amount >= 0:
                self.__balance = self.__balance - amount
                print("balance = ", self.__balance)
            else:
                print("insufficient funds")
        else:
            print("Invalid withdrawal amount.")

    # interest: applies the interest_rate to the current balance.
    def interest(self):
        self.__balance = self.__balance + \
            (self.__balance * self.__interest_rate)
        print("balance = ", self.__balance)

    def __str__(self):
        return (f"Number = {self.__number}, Name = {self.__name}, "
                f"Type = {self.__account_type}, Account Balance = {self.__balance}")

    def __repr__(self):
        return (f"Account: number={self.__number}, name={self.__name}, "
                f"type={self.__account_type}, account_balance={self.__balance}")
