class Transaction:
    """A single transaction record created and owned by an Account."""

    VALID_STATUSES = ["Pending", "Processed", "Cancelled"]

    def __init__(self, identifier, transaction_type, amount, desc,
                 status="Pending"):
        if (isinstance(identifier, int) and not isinstance(identifier, bool)
                and identifier > 0):
            self.__identifier = identifier
        else:
            self.__identifier = 0
            print("Identifier is invalid.")

        if isinstance(transaction_type, str):
            self.__transaction_type = transaction_type
        else:
            self.__transaction_type = "No Type"
            print("Transaction type is invalid.")

        if (isinstance(amount, (int, float)) and not isinstance(amount, bool)
                and amount >= 0):
            self.__amount = amount
        else:
            self.__amount = 0
            print("Amount is invalid.")

        if isinstance(desc, str):
            self.__desc = desc
        else:
            self.__desc = "No Description"
            print("Description is invalid.")

        if isinstance(status, str) and status in Transaction.VALID_STATUSES:
            self.__status = status
        else:
            self.__status = "Pending"
            print("Status is invalid.")

    @property
    def identifier(self):
        return self.__identifier

    @property
    def transaction_type(self):
        return self.__transaction_type

    @property
    def amount(self):
        return self.__amount

    @property
    def desc(self):
        return self.__desc

    @property
    def status(self):
        return self.__status

    def processed(self):
        if self.__status == "Pending":
            self.__status = "Processed"

    def cancelled(self):
        if self.__status == "Pending":
            self.__status = "Cancelled"

    def __str__(self):
        return (f"#{self.__identifier} {self.__transaction_type}: "
                f"{self.__amount} ({self.__desc}) [{self.__status}]")


class Account:
    """Parent class for all accounts. Creates and owns its transactions."""

    _next_transaction_id = 1

    def __init__(self, number, name, balance):
        if (isinstance(number, int) and not isinstance(number, bool)
                and number > 0):
            self._number = number
        else:
            self._number = 0
            print("Account number is invalid.")

        if isinstance(name, str):
            self._name = name
        else:
            self._name = "No Name"
            print("Name is invalid.")

        if (isinstance(balance, (int, float)) and not isinstance(balance, bool)
                and balance >= 0):
            self._balance = balance
        else:
            self._balance = 0
            print("Balance is invalid.")

        self._transactions = []

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
        return type(self).__name__

    @property
    def transactions(self):
        return list(self._transactions)

    def _create_transaction(self, transaction_type, amount):
        transaction = Transaction(
            Account._next_transaction_id,
            transaction_type,
            amount,
            f"{transaction_type} of {amount} on account {self._number}",
        )
        Account._next_transaction_id += 1
        transaction.processed()
        self._transactions.append(transaction)

    def deposit(self, amount):
        if (isinstance(amount, (int, float)) and not isinstance(amount, bool)
                and amount > 0):
            self._balance += amount
            self._create_transaction("Deposit", amount)
            return True
        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        if (isinstance(amount, (int, float)) and not isinstance(amount, bool)
                and amount > 0):
            if amount <= self._balance:
                self._balance -= amount
                self._create_transaction("Withdrawal", amount)
                return True
            print("Insufficient funds.")
            return False
        print("Invalid withdrawal amount.")
        return False

    def __str__(self):
        return (f"{self.account_type} #{self._number} ({self._name}): "
                f"balance {self._balance}")


class SavingsAccount(Account):
    """Earns interest and must keep a minimum balance."""

    MIN_BALANCE = 100

    def __init__(self, number, name, balance, interest_rate):
        super().__init__(number, name, balance)

        if (isinstance(interest_rate, (int, float))
                and not isinstance(interest_rate, bool) and interest_rate >= 0):
            self.__interest_rate = interest_rate
        else:
            self.__interest_rate = 0
            print("Interest rate is invalid.")

    @property
    def interest_rate(self):
        return self.__interest_rate

    def withdraw(self, amount):
        if (isinstance(amount, (int, float)) and not isinstance(amount, bool)
                and amount > 0):
            if self._balance - amount < SavingsAccount.MIN_BALANCE:
                print("Withdrawal would go below the minimum balance.")
                return False
        return super().withdraw(amount)

    def apply_interest(self):
        interest = self._balance * self.__interest_rate
        if interest > 0:
            self._balance += interest
            self._create_transaction("Interest", interest)


class EverydayAccount(Account):
    """Has a limit on how much can be withdrawn in one transaction."""

    MAX_WITHDRAW = 500

    def withdraw(self, amount):
        if (isinstance(amount, (int, float)) and not isinstance(amount, bool)
                and amount > EverydayAccount.MAX_WITHDRAW):
            print(f"Withdrawal exceeds the limit of "
                  f"{EverydayAccount.MAX_WITHDRAW}.")
            return False
        return super().withdraw(amount)


if __name__ == "__main__":
    savings = SavingsAccount(1, "Holiday", 1000, 0.05)
    everyday = EverydayAccount(2, "Spending", 2000)

    savings.deposit(500)
    savings.withdraw(1500)      # below minimum balance
    savings.withdraw(400)
    everyday.withdraw(600)      # above limit
    everyday.withdraw(200)
    savings.deposit(-5)         # invalid

    for account in (savings, everyday):
        print(account)
        for transaction in account.transactions:
            print("  ", transaction)
