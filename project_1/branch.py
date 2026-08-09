class Branch:
    def __init__(self, number, name, suburb, phone, currently_open=False):
        self.number = number
        self.name = name
        self.suburb = suburb
        self.phone = phone
        self.currently_open = currently_open
    
    def open(self):
        self.currently_open = True
        print("We are now open")
    
    def closed(self):
        self.currently_open = False
        print("We are now closed")
    
    def update_phone(self, new_num):
        self.phone = new_num
        print("Branch number updated")
        print("The new branch number is ", new_num)
    
    def __str__(self):
        status = "Open" if self.currently_open else "Closed"
        return f"Branch #{self.number}: {self.name} ({self.suburb}) - Phone: {self.phone} [{status}]"
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