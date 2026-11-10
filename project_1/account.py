from transaction import Transaction
from abc import ABC, abstractmethod
from errors.insufficient_funds_error import InsufficientFundsError


class Account(ABC):
    """The Account class represents the common state and behaviour shared
    by every kind of bank account (number, name, balance, transaction
    history).

    Account does not manage who it belongs to, that responsibility belongs
    to the Client class through add_account()."""

    # Shared counter so every Transaction created by any Account gets a
    # unique, positive identifier (Transaction requires identifier > 0).
    _next_transaction_id = 1

    def __init__(self, number, name, balance):
        if isinstance(number, int) and not isinstance(
                number, bool) and number > 0:
            self._number = number
        else:
            self._number = 0
            print("Account number is invalid.")

        if isinstance(name, str):
            self._name = name
        else:
            self._name = "No Name"
            print("Name is invalid.")

        if isinstance(balance, (int, float)) and not isinstance(
                balance, bool) and balance >= 0:
            self._balance = balance
        else:
            self._balance = 0
            print("Balance is invalid.")

        self._transactions = []

    # Getters
    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @property
    def account_type(self):
        # Derived from the class itself rather than stored, so it can never
        # drift out of sync with the object's actual type.
        return type(self).__name__

    @property
    def transactions(self):
        # Return a copy so the caller can't replace or mutate the real list.
        return list(self._transactions)

    def transaction_count(self):
        return len(self._transactions)

    def transactions_of_type(self, transaction_type):
        matches = []
        for transaction in self._transactions:
            if transaction.transaction_type == transaction_type:
                matches.append(transaction)
        return matches

    def transactions_above(self, amount):
        matches = []
        for transaction in self._transactions:
            if transaction.amount > amount:
                matches.append(transaction)
        return matches

    def display_transactions(self):
        if not self._transactions:
            print("No transactions yet.")
        for transaction in self._transactions:
            print(transaction)

    def update_account_info(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
            print("Account info updated")
        else:
            print("Invalid account info. Nothing changed.")

    def _record_transaction(self, transaction_type, amount, desc):
        transaction = Transaction(
            Account._next_transaction_id,
            transaction_type,
            amount,
            desc,
        )
        Account._next_transaction_id += 1
        transaction.processed()
        self._transactions.append(transaction)
        return transaction

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(
                amount, bool) and amount > 0:
            self._balance += amount
            self._record_transaction(
                "Deposit", amount,
                f"Deposit of {amount} to account {self._number}")
            print("balance = ", self._balance)
        else:
            print("Invalid deposit amount.")

    # Abstract because every kind of account must decide its own rules.
    # The shared steps stay here and subclasses reach them with super().
    @abstractmethod
    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(
                amount, bool) and amount > 0:
            if self._balance - amount >= 0:
                self._balance -= amount
                self._record_transaction(
                    "Withdrawal", amount,
                    f"Withdrawal of {amount} from account {self._number}")
                print("balance = ", self._balance)
            else:
                raise InsufficientFundsError(
                    f"Account {self._number}: cannot withdraw {amount}, "
                    f"balance is only {self._balance}.")
        else:
            print("Invalid withdrawal amount.")

    def __str__(self):
        return (f"Number = {self._number}, Name = {self._name}, "
                f"Type = {self.account_type}, "
                f"Account Balance = {self._balance}")

    def __repr__(self):
        return (f"{type(self).__name__}(number={self._number}, "
                f"name={self._name}, "
                f"balance={self._balance})")
