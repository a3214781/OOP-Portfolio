class Branch:
    """The Branch class is responsible for representing a physical branch
    location (branch_number, name, suburb, phone, currently_open) and its
    open/closed state.

    Branch does not track which clients prefer it, that responsibility
    belongs to the Client class."""

    def __init__(
        self, branch_number, name, suburb, phone, currently_open="Closed"
    ):
        # Branch_number must be an int, and must not be a bool value.
        if isinstance(branch_number, int) and not isinstance(
            branch_number, bool
        ):
            self.__branch_number = branch_number
        else:
            self.__branch_number = 0
            print("Branch number is invalid.")

        # The branch name must be a string value.
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = "No Name"
            print("Name is invalid.")

        # The suburb must be in the form of a string.
        if isinstance(suburb, str):
            self.__suburb = suburb
        else:
            self.__suburb = "No Suburb or Location"
            print("Suburb or Location is invalid.")

        # Phone must be a string to account for (+) numbers.
        if isinstance(phone, str):
            self.__phone = phone
        else:
            self.__phone = "No Phone"
            print("Phone Number is invalid.")

        # branch_state must be one of only two allowed states, Open or Closed.
        if isinstance(currently_open, str) and currently_open in [
            "Open",
            "Closed",
        ]:
            self.__branch_state = currently_open
        else:
            self.__branch_state = "Closed"
            print("Branch state is invalid.")

    @property
    def branch_number(self):
        return self.__branch_number

    @property
    def name(self):
        return self.__name

    @property
    def suburb(self):
        return self.__suburb

    @property
    def phone(self):
        return self.__phone

    @property
    def branch_state(self):
        return self.__branch_state

    # update_branch_info sets the name, suburb, phone and sets new
    # information together through one function, validating
    # it all together.
    def update_branch_info(self, name, suburb, phone):
        if (
            isinstance(name, str)
            and isinstance(suburb, str)
            and isinstance(phone, str)
        ):
            self.__name = name
            self.__suburb = suburb
            self.__phone = phone
            print("Branch info updated")
        else:
            print("Invalid branch info. Nothing changed.")

    # update_phone validates new_num and checking weather its a str.
    def update_phone(self, new_num):
        if isinstance(new_num, str):
            self.__phone = new_num
            print("Phone number updated")
        else:
            print("Invalid phone number. Phone not changed.")

    # The opened function changes __branch_state to "Open" if closed.
    def opened(self):
        if self.__branch_state != "Open":
            self.__branch_state = "Open"
            return "We are now open!"
        else:
            return f"We are already open!"

    # The closed function changes __branch_state to "Closed" if open.
    def closed(self):
        if self.__branch_state != "Closed":
            self.__branch_state = "Closed"
            return "We are now closed!"
        else:
            return f"We are already closed!"

    # Displays relevant branch information for clients to view.
    def __str__(self):
        return (
            f"Branch # = {self.__branch_number} Name = {self.__name} "
            f"Suburb = {self.__suburb} Phone = {self.__phone} "
            f"Status=[{self.__branch_state}]"
        )

    # Displays relevant branch information for programmers to view.
    def __repr__(self):
        return (
            f"Branch: number={self.__branch_number}, name={self.__name}, "
            f"Suburb={self.__suburb}, Phone={self.__phone}, "
            f"Status={self.__branch_state}"
        )
