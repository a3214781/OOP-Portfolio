import pytest
from errors.minimum_balance_error import MinimumBalanceError
from savings_account import SavingsAccount


class TestSavingsAccount:
    """Tests for the SavingsAccount class, checking its
    minimum balance rule and that a failed withdrawal
    leaves the account unchanged."""

    # Each test gets its own new account so tests can't affect each other.
    @pytest.fixture
    def savings(self):
        return SavingsAccount(1, "Holiday Fund", 1000, 0.05)

    def test_instance(self, savings):
        # The constructor should store every detail it was given.
        assert savings.number == 1
        assert savings.name == "Holiday Fund"
        assert savings.balance == 1000
        assert savings.interest_rate == 0.05

    def test_normal_withdrawal_works(self, savings):
        # A withdrawal that stays above the minimum balance should work.
        savings.withdraw(400)
        assert savings.balance == 600

    def test_withdraw_to_exact_minimum_works(self, savings):
        # Ending exactly on the minimum balance is allowed, not an error.
        savings.withdraw(900)
        assert savings.balance == 100

    def test_minimum_balance_raises(self, savings):
        # Dropping below the minimum balance must raise the specific error.
        with pytest.raises(MinimumBalanceError):
            savings.withdraw(950)

    def test_failed_withdrawal_changes_nothing(self, savings):
        # A failed withdrawal must leave the balance and history unchanged.
        balance_before = savings.balance
        count_before = savings.transaction_count()
        with pytest.raises(MinimumBalanceError):
            savings.withdraw(950)
        assert savings.balance == balance_before
        assert savings.transaction_count() == count_before

    def test_error_message_has_useful_details(self, savings):
        # The message should name the account, amount and minimum balance.
        with pytest.raises(MinimumBalanceError) as error_info:
            savings.withdraw(950)
        message = str(error_info.value)
        assert "Account 1" in message
        assert "950" in message
        assert "100" in message

    def test_invalid_withdrawal_amount_does_not_raise(self, savings):
        # Bad input is only printed, so the balance stays the same.
        savings.withdraw(-50)
        assert savings.balance == 1000

    def test_apply_interest(self, savings):
        # Interest should be added to the balance and recorded.
        savings.apply_interest()
        assert savings.balance == 1050
        assert savings.transaction_count() == 1
