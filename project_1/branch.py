class Branch:
    # Represents a bank branch with contact details and an open/closed state.
    
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
    
    # UPDATED: now validates like every other setter in the project — previously had no checks at all
    def updateInfo(self, name, suburb, phone):
        if isinstance(name, str) and isinstance(suburb, str) and isinstance(phone, str):
            self.__name = name
            self.__suburb = suburb
            self.__phone = phone
            print("Branch info updated")
        else:
            print("Invalid branch info. Nothing changed.")
            
    # UPDATED: now validates like every other setter — previously accepted anything
    def update_phone(self, new_num):
        if isinstance(new_num, str):
            self.__phone = new_num
            print("Phone number updated")
        else:
            print("Invalid phone number. Phone not changed.")

    # Behaviour: the only way __branch_state can become "Open"
    def opened(self):
        self.__branch_state = "Open"
        print("We are now open!")

    # Behaviour: the only way __branch_state can become "Closed"
    def closed(self):
        self.__branch_state = "Closed"
        print("We are now closed!")

    # UPDATED: now validates like every other setter — previously accepted anything
    def update_phone(self, new_num):
        self.__phone = new_num
        print("Phone number updated")
        print("The new phone number is ", new_num)

    def __str__(self):
        return (f"Branch # = {self.__branch_number} Name = {self.__name} "
                f"Suburb = {self.__suburb} Phone = {self.__phone} "
                f"Status=[{self.__branch_state}]")

    def __repr__(self):
        return (f"Branch: number={self.__branch_number}, name={self.__name}, "
                f"Suburb={self.__suburb}, Phone={self.__phone}, "
                f"Status={self.__branch_state}")


'''
# Branch 1
branch_1 = Branch(1, "main", "Adelaide", "0431 324 432")
branch_1.open()
branch_1.closed()
branch_1.update_phone("0432 234 321")

# Branch 2
branch_2 = Branch(2, "remote_branch", "Alice Springs", "0432 657 423")
branch_2.open()
branch_2.closed()
branch_2.update_phone("0213 543 635")
'''
