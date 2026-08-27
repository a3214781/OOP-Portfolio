from account import Account
from branch import Branch

class Client:
    """The Client class is responsible for representing a client's identity
    and contact details (number, name, email, age), for managing which
    Account objects the client currently holds, and for tracking which
    Branch the client prefers, if any.

    Client does not manage account balances, transaction history, or
    branch operations directly — that responsibility belongs to the
    Account, Transaction, and Branch classes respectively.
    """
        
    def __init__(self, number, name, email, age):
        # number must be a positive int, not a bool
        if isinstance(number, int) and not isinstance(number, bool):
            self.__number = number
        else:
            self.__number = 0
            print("Client number is invalid.")

        # name must be a string
        if isinstance(name, str): 
            self.__name = name
        else:
            self.__name = "No Name"
            print("Name is invalid.")

        # email must be a string that looks like an email (contains "@")
        if isinstance(email, str) and "@" in email:
            self.__email = email
        else:
            self.__email = "No Email"
            print("Email is invalid.")

        # age must be a non-negative int, not a bool
        if isinstance(age, int) and not isinstance(age, bool) and age >= 0:
            self.__age = age
        else:
            self.__age = 0
            print("Age is invalid.")
            
        # Aggregation: every client starts with no accounts
        self.__accounts = []

        # Association: every client starts with no preferred branch
        self.__preferred_branch = None

    # Getters — number, name, and age have no setters, so this is the only way to read them
    def get_number(self):
        return self.__number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    # Setter: only email can be changed after creation, same validation as the constructor
    def set_email(self, new_email):
        if isinstance(new_email, str) and "@" in new_email:
            self.__email = new_email
            print("Email updated")
        else:
            print("Email is invalid. Email not changed.")
            
        # Aggregation: add an Account to this client, rejecting duplicates and wrong types
    def add_account(self, account):
        if not isinstance(account, Account):
            print("Invalid object. Only Account objects can be added.")
            return
        if account in self.__accounts:
            print("This account is already assigned to this client.")
            return
        self.__accounts.append(account)
        print("Account added.")

    # Aggregation: remove an Account from this client without deleting the object itself
    def remove_account(self, account):
        if not isinstance(account, Account):
            print("Invalid object. Only Account objects can be removed.")
            return
        if account not in self.__accounts:
            print("This account is not assigned to this client.")
            return
        self.__accounts.remove(account)
        print("Account removed.")

    # Returns a copy so external code can't bypass add_account()/remove_account()
    def get_accounts(self):
        return list(self.__accounts)

    # Association: set a preferred Branch, rejecting anything that isn't one
    def set_preferred_branch(self, branch):
        if not isinstance(branch, Branch):
            print("Invalid object. Preferred branch must be a Branch object.")
            return
        self.__preferred_branch = branch
        print("Preferred branch updated.")

    def get_preferred_branch(self):
        return self.__preferred_branch

    def __str__(self):
        return (f"Number = {self.__number}, Name = {self.__name}, "
                f"Email = {self.__email}, Age = {self.__age}")

    def __repr__(self):
        return (f"Client: number={self.__number}, name={self.__name}, "
                f"email={self.__email}, age={self.__age}")
