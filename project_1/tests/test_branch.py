import pytest
from branch import Branch


class TestBranch:
    """Tests for the Branch class checking its details, its state,
    and its update methods."""

    # Each test gets a new branch that starts closed.
    @pytest.fixture
    def branch(self):
        return Branch(1, "City", "Adelaide", "+61 431 324 432")

    def test_instance(self, branch):
        # The constructor should store all details individually.
        assert branch.branch_number == 1
        assert branch.name == "City"
        assert branch.suburb == "Adelaide"
        assert branch.phone == "+61 431 324 432"
        assert branch.branch_state == "Closed"

    def test_invalid_branch_number_uses_zero(self, capsys):
        # A string is not a valid number, so 0 should be used instead.
        branch = Branch("1", "City", "Adelaide", "+61 431 324 432")
        assert branch.branch_number == 0
        assert "Branch number is invalid." in capsys.readouterr().out

    def test_invalid_name_uses_default(self, capsys):
        # A number is'nt a valid name, so a default should be used.
        branch = Branch(1, 5, "Adelaide", "+61 431 324 432")
        assert branch.name == "No Name"
        assert "Name is invalid." in capsys.readouterr().out

    def test_invalid_suburb_uses_default(self, capsys):
        # A number is'nt a valid suburb, so a default should be used.
        branch = Branch(1, "City", 5, "+61 431 324 432")
        assert branch.suburb == "No Suburb or Location"
        assert "Suburb or Location is invalid." in capsys.readouterr().out

    def test_invalid_phone_uses_default(self, capsys):
        # A number is'nt a valid phone, so a default should be used.
        branch = Branch(1, "City", "Adelaide", 431324432)
        assert branch.phone == "No Phone"
        assert "Phone Number is invalid." in capsys.readouterr().out

    def test_invalid_state_defaults_to_closed(self, capsys):
        """ Only "Open" or "Closed" are allowed, so
        anything else set to default (closed). """
        branch = Branch(1, "City", "Adelaide", "+61 431 324 432",
                        "Maybe")
        assert branch.branch_state == "Closed"
        assert "Branch state is invalid." in capsys.readouterr().out

    def test_opened_when_closed(self, branch):
        # Opening a closed branch should change its state.
        assert branch.opened() == "We are now open!"
        assert branch.branch_state == "Open"

    def test_opened_when_already_open(self):
        # Opening a branch that is already open changes nothing.
        branch = Branch(1, "City", "Adelaide", "+61 431 324 432",
                        "Open")
        assert branch.opened() == "We are already open!"
        assert branch.branch_state == "Open"

    def test_closed_when_open(self):
        # Closing an open branch should change its state.
        branch = Branch(1, "City", "Adelaide", "+61 431 324 432",
                        "Open")
        assert branch.closed() == "We are now closed!"
        assert branch.branch_state == "Closed"

    def test_closed_when_already_closed(self, branch):
        # Closing a branch that is already closed changes nothing.
        assert branch.closed() == "We are already closed!"
        assert branch.branch_state == "Closed"

    def test_update_branch_info(self, branch):
        # All three details should change together when they are valid.
        branch.update_branch_info("Norwood", "Norwood", "+61 8 1234 5678")
        assert branch.name == "Norwood"
        assert branch.suburb == "Norwood"
        assert branch.phone == "+61 8 1234 5678"

    def test_update_branch_info_invalid_changes_nothing(self, branch):
        # One invalid value means nothing should change at all.
        branch.update_branch_info(5, "Norwood", "+61 8 1234 5678")
        assert branch.name == "City"
        assert branch.suburb == "Adelaide"
        assert branch.phone == "+61 431 324 432"

    def test_update_phone(self, branch):
        # A valid string should replace the phone number.
        branch.update_phone("+61 400 111 222")
        assert branch.phone == "+61 400 111 222"

    def test_update_phone_invalid_changes_nothing(self, branch):
        # A number is not a valid phone, so the old phone should stay.
        branch.update_phone(4321)
        assert branch.phone == "+61 431 324 432"

    def test_str_shows_status(self, branch):
        # The user-friendly text should show branch state.
        assert "Status=[Closed]" in str(branch)

    def test_repr_shows_every_detail(self, branch):
        # The repr text should name the class and the branch number.
        assert "Branch: number=1" in repr(branch)
