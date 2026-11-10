from account import Account
from branch import Branch
from errors.account_not_found_error import AccountNotFoundError
from errors.finance_error import FinanceError


class Client:
    """The Client class is responsible for representing a client's identity
    and contact details, for managing which Account objects the client
    currently holds, and for tracking which Branch the client prefers, if any.

    Client does not manage account balances, transaction history, or
    branch operations directly."""

    def __init__(self, number, name, email, age):
        # The number must be an int and not a bool, so every
        # client can be identified by a real number.
        if isinstance(number, int) and not isinstance(number, bool):
            self.__number = number
        else:
            self.__number = 0
            print("Client number is invalid.")

        # The name must be a string so it can be printed as readable text.
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = "No Name"
            print("Name is invalid.")

        # The email must be a string containing "@". Anything stricter would be
        # over-filtering.
        if isinstance(email, str) and "@" in email:
            self.__email = email
        else:
            self.__email = "No Email"
            print("Email is invalid.")

        # The age must be an int that is zero or more and not a bool.
        if isinstance(age, int) and not isinstance(age, bool) and age >= 0:
            self.__age = age
        else:
            self.__age = 0
            print("Age is invalid.")

        # Every client starts with no accounts.
        self.__accounts = {}

        # Every client starts with no preferred branch.
        self.__preferred_branch = None

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def age(self):
        return self.__age

    # Accounts returns a copy of the dict so a caller can't add or remove
    # accounts without going through add_account and remove_account.
    @property
    def accounts(self):
        return dict(self.__accounts)

    @property
    def preferred_branch(self):
        return self.__preferred_branch

    # Sets the email can change after creation, so it gets the same
    # "@" check as the constructor to keep bad data out.
    @email.setter
    def email(self, new_email):
        if new_email == self.__email:
            print("This email is already set")
        else:
            if isinstance(new_email, str) and "@" in new_email:
                self.__email = new_email
                print("Email updated")
            else:
                print("Email is invalid. Email not changed.")

    # set_preferred_branch sets the preferred Branch, rejecting anything
    # that isn't a Branch object.
    @preferred_branch.setter
    def preferred_branch(self, branch):
        if isinstance(branch, Branch):
            self.__preferred_branch = branch
            print("Preferred branch updated.")
        else:
            print("Invalid object. Preferred branch must be a Branch object.")
            return

    # add_account stores an Account under its account number so it can be
    # found again quickly.
    def add_account(self, account):
        if isinstance(account, Account):
            if account.number in self.__accounts:
                print("This account is already assigned to this client.")
            else:
                self.__accounts[account.number] = account
                print("Account added.")
        else:
            print("Invalid object. Only Account objects can be added.")

    # get_account looks up one Account by its number. It raises a
    # FinanceError when the client doesn't hold it.
    def get_account(self, number):
        if number in self.__accounts:
            return self.__accounts[number]
        else:
            raise AccountNotFoundError(
                f"Client {self.__number}: no account with number {number}."
            )

    # Remove_account takes an Account off this client by its number without
    # deleting the Account object itself.
    def remove_account(self, number):
        if number in self.__accounts:
            del self.__accounts[number]
            print("Account removed.")
        else:
            raise AccountNotFoundError(
                f"Client {self.__number}: no account with number {number}."
            )

    # Withdraw_from looks up the account and withdraws from it. The
    # try/except lives here, inside the class, so rule breaks are reported
    # with a message.
    def withdraw_from(self, number, amount):
        try:
            account = self.get_account(number)
            account.withdraw(amount)
        except FinanceError as error:
            print(f"Withdrawal failed: {error}")

    # __str__ gives a readable line for users who print a client.
    def __str__(self):
        return (
            f"Number = {self.__number}, Name = {self.__name}, "
            f"Email = {self.__email}, Age = {self.__age}"
        )

    # __repr__ gives an unambiguous line showing every attribute, which is
    # what a programmer needs when debugging.
    def __repr__(self):
        return (
            f"Client: number={self.__number}, name={self.__name}, "
            f"email={self.__email}, age={self.__age}"
        )
