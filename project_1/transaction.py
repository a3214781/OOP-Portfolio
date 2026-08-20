class Transaction:
    def __init__(self, identifier, trasaction_type, amount, desc, status="Pending"):
        self.__identifier = identifier
        self.__trasaction_type = trasaction_type
        self.__amount = amount
        self.__desc = desc
        self.__status = status

    def processed(self):
        self.status = "Processed"
        print("transaction processes sucsessfully")

    def cancelled(self):
        self.status = "Cancelled"
        print("transaction cancelled sucsessfully")

    def set_desc(self, new_desc):
        if isinstance(new_desc, str):
        # BUG: fix later
            self.desc = new_desc
    
    def get_desc(self):
        return self.__desc
    
    '''
    def set_identifier(self, new_id):
        if isinstance(new_id, int) and not isinstance(new_id, bool) and new_id > 0:
            self.__identifier = new_id
    '''
      
    def get_identifier(self):
        return self.__identifier
    
    def set_trasaction_type(self, new_type):
        if isinstance(new_type, str):
            self.__trasaction_type = new_type
        
    def get_trasaction_type(self):
        return self.__trasaction_type
        
    def __str__(self):
        return f"{self.__identifier}, Type = {self.__trasaction_type}, Amount = {self.__amount}, Description = \"{self.__desc}\", Status = {self.__status}"
    # Include the transaction identifier, type, amount, description, and current status.

    def __repr__(self):
        return f"Transaction: identifier={self.__identifier}, trasaction_type={self.__trasaction_type}, amount={self.__amount}, desc={self.__desc}, status={self.__status}"
    # Include enough attribute values to identify the object’s current state.

'''
# Transaction 1
trasnaction_1 = Transaction(1, "Purchase", 15.5, "bought lunch")
print(trasnaction_1)
trasnaction_1.processed()
print(trasnaction_1)
trasnaction_1.description("new description")
print(trasnaction_1)
print("---------------")
# Transaction 2
trasnaction_2 = Transaction(2, "Purchase", 67.8, "new shirt")
print(trasnaction_2)
trasnaction_2.processed()
print(trasnaction_2)
trasnaction_2.description("shirt new")
print(trasnaction_2)
'''
