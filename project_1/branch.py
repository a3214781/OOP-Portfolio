class Branch:
    def __init__(self, number, name, suburb, phone, currently_open=False):
        self.__number = number
        self.__name = name
        self.__suburb = suburb
        self.__phone = phone
        self.__currently_open = currently_open
        
    def updateInfo(self, name, suburb, phone):
        self.__name = name
        self.__suburb = suburb
        if isinstance(phone, (int, float)):
            self.__phone = phone
        
    def opened(self):
        self.__currently_open = True
        print("We are now open!")

    def closed(self):
        self.__currently_open = False
        print("We are now closed!")

    def update_phone(self, new_num):
        self.__phone = new_num
        print("Branch number updated")
        print("The new branch number is ", new_num)

    def __str__(self):
        status = "Open" if self.__currently_open else "Closed"
        return f"Branch # = {self.__number} Name = {self.__name} Suburb = {self.__suburb} Phone = {self.__phone} Status=[{status}]"

    def __repr__(self):
        return f"Branch: number={self.__number}, name={self.__name}, Suburb={self.__suburb}, Phone={self.__phone} Status={self.__currently_open}"

        # Include enough attribute values to identify the object’s current state.
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
