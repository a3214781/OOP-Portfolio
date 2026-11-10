import pytest
from errors.account_not_found_error import AccountNotFoundError
from client import Client
from everyday_account import EverydayAccount
from savings_account import SavingsAccount


class TestClient:
    """Tests for the Client class, checking how it holds accounts and that it
    catches Finance errors inside the class so the program carries on."""

    # Fresh accounts for every test so tests can't affect each other.
    @pytest.fixture
    def savings(self):
        return SavingsAccount(1, "Holiday Fund", 1000, 0.05)

    @pytest.fixture
    def everyday(self):
        return EverydayAccount(2, "Spending", 2000)

    # A client holding both accounts, so tests can use the Client methods.
    @pytest.fixture
    def client(self, savings, everyday):
        new_client = Client(1, "Alessio", "alessio@gmail.com", 19)
        new_client.add_account(savings)
        new_client.add_account(everyday)
        return new_client

    def test_instance(self, client):
        # The constructor stores all details given.
        assert client.number == 1
        assert client.name == "Alessio"
        assert client.email == "alessio@gmail.com"
        assert client.age == 19

    def test_get_account_returns_the_account(self, client, savings):
        # Looking up a held account number should return that account.
        assert client.get_account(1) is savings

    def test_get_account_missing_raises(self, client):
        # Looking up an account the client doesn't hold must raise.
        with pytest.raises(AccountNotFoundError):
            client.get_account(99)

    def test_missing_account_message_has_useful_details(self, client):
        # The message should name the client and the missing number.
        with pytest.raises(AccountNotFoundError) as error_info:
            client.get_account(99)
        message = str(error_info.value)
        assert "Client 1" in message
        assert "99" in message

    def test_remove_account(self, client):
        # A removed account should no longer be held by the client.
        client.remove_account(1)
        assert 1 not in client.accounts

    def test_remove_account_missing_raises(self, client):
        # Removing an account the client doesn't hold must raise.
        with pytest.raises(AccountNotFoundError):
            client.remove_account(99)

    def test_duplicate_account_is_rejected(self, client, savings):
        # Adding the same account number twice should keep only one.
        client.add_account(savings)
        assert len(client.accounts) == 2

    def test_withdraw_from_works(self, client, savings):
        # A valid withdrawal through the client should reach the account.
        client.withdraw_from(1, 400)
        assert savings.balance == 600

    def test_withdraw_from_catches_rule_break(self, client, savings, capsys):
        # The error should be caught inside the class, reported, and leave
        # the balance alone.
        client.withdraw_from(1, 5000)
        assert "Withdrawal failed" in capsys.readouterr().out
        assert savings.balance == 1000

    def test_withdraw_from_missing_account_carries_on(self, client, capsys):
        # A missing account should be reported without stopping the program.
        client.withdraw_from(99, 50)
        assert "Withdrawal failed" in capsys.readouterr().out
