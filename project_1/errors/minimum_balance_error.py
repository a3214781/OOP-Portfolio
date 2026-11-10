from errors.finance_error import FinanceError


class MinimumBalanceError(FinanceError):
    """Raised when a withdrawal would take a SavingsAccount below its
    minimum balance."""
