from transaction import Transaction

class Account:
    """The Account class represents the common state and behaviour shared
    by every kind of bank account (number, name, balance, transaction
    history).

    Account does not manage who it belongs to, that responsibility belongs
    to the Client class through add_account()."""

    # Shared counter so every Transaction created by any Account gets a
    # unique, positive identifier (Transaction requires identifier > 0).
    _next_transaction_id = 1

    def __init__(self, number, name, balance):
        if isinstance(number, int) and not isinstance(number, bool) and number > 0:
            self._number = number
        else:
            self._number = 0
            print("Account number is invalid.")

        if isinstance(name, str):
            self._name = name
        else:
            self._name = "No Name"
            print("Name is invalid.")

        if isinstance(balance, (int, float)) and not isinstance(balance, bool) and balance >= 0:
            self._balance = balance
        else:
            self._balance = 0
            print("Balance is invalid.")

        self._transactions = []

    # Getters
    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def get_balance(self):
        return self._balance

    def get_account_type(self):
        # Derived from the class itself rather than stored, so it can never
        # drift out of sync with the object's actual type.
        return type(self).__name__

    def get_transactions(self):
        # Return a copy so the caller can't replace or mutate the real list.
        return list(self._transactions)

    number = property(get_number)
    name = property(get_name)
    balance = property(get_balance)
    account_type = property(get_account_type)
    transactions = property(get_transactions)

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
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            self._balance += amount
            self._record_transaction("Deposit", amount, f"Deposit of {amount} to account {self._number}")
            print("balance = ", self._balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            if self._balance - amount >= 0:
                self._balance -= amount
                self._record_transaction("Withdrawal", amount, f"Withdrawal of {amount} from account {self._number}")
                print("balance = ", self._balance)
            else:
                print("insufficient funds")
        else:
            print("Invalid withdrawal amount.")

    def __str__(self):
        return (f"Number = {self._number}, Name = {self._name}, "
                f"Type = {self.get_account_type()}, Account Balance = {self._balance}")

    def __repr__(self):
        return (f"{type(self).__name__}(number={self._number}, name={self._name}, "
                f"balance={self._balance})")

class SavingsAccount(Account):
    """A Savings Account earns interest but must stay above a minimum balance."""

    def __init__(self, number, name, balance, interest_rate, minimum_balance):
        super().__init__(number, name, balance)

        if isinstance(interest_rate, (int, float)) and not isinstance(interest_rate, bool) and interest_rate >= 0:
            self.__interest_rate = interest_rate
        else:
            self.__interest_rate = 0
            print("Interest rate is invalid.")

        if isinstance(minimum_balance, (int, float)) and not isinstance(minimum_balance, bool) and minimum_balance >= 0:
            self.__minimum_balance = minimum_balance
        else:
            self.__minimum_balance = 0
            print("Minimum balance is invalid.")

    def get_interest_rate(self):
        return self.__interest_rate

    def get_minimum_balance(self):
        return self.__minimum_balance

    interest_rate = property(get_interest_rate)
    minimum_balance = property(get_minimum_balance)

    def apply_interest(self):
        interest_amount = self._balance * self.__interest_rate
        self._balance += interest_amount
        self._record_transaction("Interest", interest_amount, f"Interest applied to account {self._number}")
        print("balance = ", self._balance)

    # can't withdraw below minimum_balance
    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            if self._balance - amount >= self.__minimum_balance:
                super().withdraw(amount)
            else:
                print("insufficient funds: cannot go below minimum balance")
        else:
            print("Invalid withdrawal amount.")

class EverydayAccount(Account):
    """An Everyday Account has a cap on how much can be withdrawn in one transaction."""

    MAX_WITHDRAW = 500

    def __init__(self, number, name, balance):
        super().__init__(number, name, balance)

    def get_max_withdrawal(self):
        return EverydayAccount.MAX_WITHDRAW

    max_withdraw = property(get_max_withdrawal)

    # rejects any single withdrawal over the cap
    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            if amount > EverydayAccount.MAX_WITHDRAW:
                print(f"withdrawal exceeds max limit of {EverydayAccount.MAX_WITHDRAW}")
            else:
                super().withdraw(amount)
        else:
            print("Invalid withdrawal amount.")
