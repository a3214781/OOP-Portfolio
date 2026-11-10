from account import Account
from errors.minimum_balance_error import MinimumBalanceError


class SavingsAccount(Account):
    """The SavingsAccount class is responsible for the rules that make an
    account a savings account, earning interest and balance staying above
    the minimum.

    SavingsAccount does not store the number, name, balance or transaction
    history, because that responsibility belongs to the Account class it
    inherits from."""

    # The minimum is a class constant so every savings account shares one
    # value and it can be read without creating an object.
    MIN_BALANCE = 100

    def __init__(self, number, name, balance, interest_rate):
        # The shared details are validated and stored by Account
        super().__init__(number, name, balance)

        # The interest rate must be a number that is zero or more (and not a
        # bool), because a negative rate would shrink the savings each time.
        # It is private since only this class applies interest.
        if isinstance(interest_rate, (int, float)) and not isinstance(
                interest_rate, bool) and interest_rate >= 0:
            self.__interest_rate = interest_rate
        else:
            self.__interest_rate = 0
            print("Interest rate is invalid.")

    @property
    def interest_rate(self):
        return self.__interest_rate

    @property
    def minimum_balance(self):
        return SavingsAccount.MIN_BALANCE

    def apply_interest(self):
        """apply_interest is unique to savings accounts, which earn interest,
        so it lives here and not in Account. It records a transaction
        so the history shows where the extra money came from."""
        interest_amount = self._balance * self.__interest_rate
        self._balance += interest_amount
        self._record_transaction(
            "Interest", interest_amount,
            f"Interest applied to account {self._number}")
        print("balance = ", self._balance)

    # Withdraw overrides Account.withdraw to add the savings rule. The
    # minimum balance is checked so FinanceError can be raised before
    # any change, so a failed withdrawal leaves everything untouched.
    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(
                amount, bool) and amount > 0:
            if self._balance - amount >= SavingsAccount.MIN_BALANCE:
                super().withdraw(amount)
            else:
                raise MinimumBalanceError(
                    f"Account {self._number}: cannot withdraw {amount}, "
                    f"balance is {self._balance} and the minimum balance "
                    f"is {SavingsAccount.MIN_BALANCE}.")
        else:
            print("Invalid withdrawal amount.")
