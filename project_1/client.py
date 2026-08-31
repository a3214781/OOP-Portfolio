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

        # email must be a string that contains "@" symbol (forms a valid email)
        if isinstance(email, str) and "@" in email:
            self.__email = email
        else:
            self.__email = "No Email"
            print("Email is invalid.")

        # age must be a positive int and not a boolean (1,0)
        if isinstance(age, int) and not isinstance(age, bool) and age >= 0:
            self.__age = age
        else:
            self.__age = 0
            print("Age is invalid.")

        # every client starts with no accounts and can be added through add_account() function
        self.__accounts = []

        # every client starts with no preferred branch and can be added through set_preferred_branch() function
        self.__preferred_branch = None

    # Getters: retrieve private variable values from __init__ function
    def get_number(self):
        return self.__number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    def get_accounts(self):
        return self.__accounts

    def get_preferred_branch(self):
        return self.__preferred_branch

    # Setters: used to alter previously named parameters in the constructor
    #
    # set_email:  email can be changed after creation and has the same validation as the constructor ("@")
    def set_email(self, new_email):
        if new_email == self.__email:
            print("This email is already set")
        else:
            if isinstance(new_email, str) and "@" in new_email:
                self.__email = new_email
                print("Email updated")
            else:
                print("Email is invalid. Email not changed.")

    # add_account: add an Account to this client. Rejects anything that is not an Account type, or duplicates
    def add_account(self, account):
        if isinstance(account, Account):
            if account in self.__accounts:
                print("This account is already assigned to this client.")
                return
            else:
                self.__accounts.append(account)
                print("Account added.")
        else:
            print("Invalid object. Only Account objects can be added.")
            return

    # remove_account: remove an Account from this client without deleting the object itself to be reused later
    def remove_account(self, account):
        if isinstance(account, Account):
            if account not in self.__accounts:
                print("This account is not assigned to this client.")
                return
            else:
                self.__accounts.remove(account)
                print("Account removed.")
        else:
            print("Invalid object. Only Account objects can be removed.")
            return

    # set_preferred_branch: set a preferred Branch, rejecting anything that isn't a Branch object
    def set_preferred_branch(self, branch):
        if isinstance(branch, Branch):
            self.__preferred_branch = branch
            print("Preferred branch updated.")
        else:
            print("Invalid object. Preferred branch must be a Branch object.")
            return

    def __str__(self):
        return (f"Number = {self.__number}, Name = {self.__name}, "
                f"Email = {self.__email}, Age = {self.__age}")

    def __repr__(self):
        return (f"Client: number={self.__number}, name={self.__name}, "
                f"email={self.__email}, age={self.__age}")
