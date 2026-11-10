from errors.finance_error import FinanceError


class WithdrawalLimitError(FinanceError):
    """Raised when a single withdrawal from an EverydayAccount is larger
    than the allowed limit."""
