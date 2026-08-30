class Branch:
    # Represents a bank branch with contact details and an open/closed state.

    """The Branch class is responsible for representing a Branch of the 
    bank through (branch_number, name, suburb, phone, currently_open).

    The branch class is responsible for holding clients and executing transactions        
    Branch does not manage who is assigned to it, that responsibility belongs 
    to the Client class."""

    def __init__(self, branch_number, name, suburb, phone, currently_open="Closed"):
        # branch_number must be an int, not a bool
        if isinstance(branch_number, int) and not isinstance(branch_number, bool):
            self.__branch_number = branch_number
        else:
            self.__branch_number = 0
            print("Branch number is invalid.")

        # name must be a string
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = "No Name"
            print("Name is invalid.")

        # suburb must be a string
        if isinstance(suburb, str):
            self.__suburb = suburb
        else:
            self.__suburb = "No Suburb or Location"
            print("Suburb or Location is invalid.")

        # phone must be a string
        if isinstance(phone, str):
            self.__phone = phone
        else:
            self.__phone = "No Phone"
            print("Phone Number is invalid.")

        # branch_state must be one of the two allowed states
        if isinstance(currently_open, str) and currently_open in ["Open", "Closed"]:
            self.__branch_state = currently_open
        else:
            self.__branch_state = "Closed"
            print("Branch state is invalid.")

    # NEW: getters — every other class has these, Branch was missing them entirely
    def get_branch_number(self):
        return self.__branch_number

    def get_name(self):
        return self.__name

    def get_suburb(self):
        return self.__suburb

    def get_phone(self):
        return self.__phone

    def get_branch_state(self):
        return self.__branch_state

    # updateInfo: validates name, suburb, phone and sets new information together through one function
    def updateInfo(self, name, suburb, phone):
        if isinstance(name, str) and isinstance(suburb, str) and isinstance(phone, str):
            self.__name = name
            self.__suburb = suburb
            self.__phone = phone
            print("Branch info updated")
        else:
            print("Invalid branch info. Nothing changed.")

    # update_phone: validates new_num and checking weather its a str
    def update_phone(self, new_num):
        if isinstance(new_num, str):
            self.__phone = new_num
            print("Phone number updated")
        else:
            print("Invalid phone number. Phone not changed.")

    # opened: the only way __branch_state can become "Open"
    def opened(self):
        self.__branch_state = "Open"
        print("We are now open!")

    # closed: the only way __branch_state can become "Closed"
    def closed(self):
        self.__branch_state = "Closed"
        print("We are now closed!")

    def __str__(self):
        return (f"Branch # = {self.__branch_number} Name = {self.__name} "
                f"Suburb = {self.__suburb} Phone = {self.__phone} "
                f"Status=[{self.__branch_state}]")

    def __repr__(self):
        return (f"Branch: number={self.__branch_number}, name={self.__name}, "
                f"Suburb={self.__suburb}, Phone={self.__phone}, "
                f"Status={self.__branch_state}")
