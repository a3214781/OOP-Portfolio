from errors.finance_error import FinanceError


class AccountNotFoundError(FinanceError):
    """Raised when a Client is asked for an account number it doesn't hold."""
