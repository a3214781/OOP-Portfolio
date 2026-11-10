from errors.finance_error import FinanceError


class InsufficientFundsError(FinanceError):
    """Raised when a withdrawal is bigger than the balance, so the account
    would go negative."""
