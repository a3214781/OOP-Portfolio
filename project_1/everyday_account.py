from account import Account
from errors.withdrawal_limit_error import WithdrawalLimitError


class EverydayAccount(Account):
    """The EverydayAccount class is responsible for the rule that makes an
    account an everyday account which is a single withdrawal can't be
    larger than a fixed limit (MAX_WITHDRAW).

    EverydayAccount does not store the number, name, balance or transaction
    history, because that responsibility belongs to the Account class it
    inherits from."""

    # The limit is a class constant so every everyday account shares one
    # value and it can be read without creating an object.
    MAX_WITHDRAW = 500

    def __init__(self, number, name, balance):
        # Everyday accounts have no extra details, so Account validates and
        # stores everything.
        super().__init__(number, name, balance)

    @property
    def max_withdrawal(self):
        return EverydayAccount.MAX_WITHDRAW

    # Withdraw overrides Account.withdraw to add the everyday rule. The limit
    # is checked so FinanceError is raised before any change.
    def withdraw(self, amount):
        if (
            isinstance(amount, (int, float))
            and not isinstance(amount, bool)
            and amount > 0
        ):
            if amount > EverydayAccount.MAX_WITHDRAW:
                raise WithdrawalLimitError(
                    f"Account {self._number}: cannot withdraw {amount}, "
                    f"the limit for one withdrawal is "
                    f"{EverydayAccount.MAX_WITHDRAW}."
                )
            else:
                super().withdraw(amount)
        else:
            print("Invalid withdrawal amount.")
