import pytest
from everyday_account import EverydayAccount
from errors.insufficient_funds_error import InsufficientFundsError
from errors.withdrawal_limit_error import WithdrawalLimitError


class TestEverydayAccount:
    """Tests for the EverydayAccount class, checking its withdrawal limit and
    the shared insufficient funds rule inherited from Account."""

    # Each test gets its own fresh account so tests can't affect each other.
    @pytest.fixture
    def everyday(self):
        return EverydayAccount(2, "Spending", 2000)

    # A small balance so a withdrawal can be within the limit but too big.
    @pytest.fixture
    def low_balance(self):
        return EverydayAccount(3, "Low", 100)

    def test_instance(self, everyday):
        # The constructor should store every detail it was given.
        assert everyday.number == 2
        assert everyday.name == "Spending"
        assert everyday.balance == 2000

    def test_normal_withdrawal_works(self, everyday):
        # A withdrawal within the limit should come off the balance.
        everyday.withdraw(200)
        assert everyday.balance == 1800

    def test_withdraw_exactly_the_limit_works(self, everyday):
        # Withdrawing exactly the limit is allowed, only more is an error.
        everyday.withdraw(500)
        assert everyday.balance == 1500

    def test_limit_raises(self, everyday):
        # A withdrawal over the limit must raise, even if the balance can
        # cover it.
        with pytest.raises(WithdrawalLimitError):
            everyday.withdraw(600)

    def test_limit_failure_changes_nothing(self, everyday):
        # A failed withdrawal must leave the balance and history unchanged.
        balance_before = everyday.balance
        count_before = everyday.transaction_count()
        with pytest.raises(WithdrawalLimitError):
            everyday.withdraw(600)
        assert everyday.balance == balance_before
        assert everyday.transaction_count() == count_before

    def test_limit_message_has_useful_details(self, everyday):
        # The message should name the account, amount and limit.
        with pytest.raises(WithdrawalLimitError) as error_info:
            everyday.withdraw(600)
        message = str(error_info.value)
        assert "Account 2" in message
        assert "600" in message
        assert "500" in message

    def test_insufficient_funds_raises(self, low_balance):
        # Withdrawing more than the balance holds must raise, not go negative.
        with pytest.raises(InsufficientFundsError):
            low_balance.withdraw(200)

    def test_insufficient_funds_changes_nothing(self, low_balance):
        # A failed withdrawal must leave the balance and history unchanged.
        with pytest.raises(InsufficientFundsError):
            low_balance.withdraw(200)
        assert low_balance.balance == 100
        assert low_balance.transaction_count() == 0

    def test_insufficient_funds_message_has_useful_details(self, low_balance):
        # The message should name the account, amount and balance.
        with pytest.raises(InsufficientFundsError) as error_info:
            low_balance.withdraw(200)
        message = str(error_info.value)
        assert "Account 3" in message
        assert "200" in message
        assert "100" in message
