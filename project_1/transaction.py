class Transaction:
    def __init__(self, identifier, trasaction_type, amount, desc, status="Pending"):
        self.identifier = identifier
        self.trasaction_type = trasaction_type
        self.amount = amount
        self.desc = desc
        self.status = status
        
    def processed(self):
        self.status = "Processed"
        print("transaction processes sucsessfully")
            
    def cancelled(self):
        self.status = "Cancelled"
        print("transaction cancelled sucsessfully")
    
    def description(self, new_desc):
        self.desc = new_desc
        print("description updated sucsessfully")
        
    def __str__(self):
        return f"{self.identifier} {self.trasaction_type} {self.amount} {self.desc} {self.status}"

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