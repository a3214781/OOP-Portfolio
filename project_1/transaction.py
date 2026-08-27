class Transaction:
    def __init__(self, identifier, transaction_type, amount, desc, status="Pending"):
        # Represents a single financial transaction with basic validation.
        if isinstance(identifier, int) and not isinstance(identifier, bool) and identifier > 0:
            self.__identifier = identifier
        else:
            self.__identifier = 0
            print("Identifier is invalid.")

        # transaction_type must be a string
        if isinstance(transaction_type, str):
            self.__transaction_type = transaction_type
        else:
            self.__transaction_type = "No Type"
            print("Transaction type is invalid.")
        
        # amount must be a non-negative number, not a bool
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount >= 0:
            self.__amount = amount
        else:
            self.__amount = 0
            print("Amount is invalid.")

        # desc must be a string
        if isinstance(desc, str):
            self.__desc = desc
        else:
            self.__desc = "No Description"
            print("Description is invalid.")

        # status must be one of the three allowed states
        if isinstance(status, str) and status in ["Pending", "Processed", "Cancelled"]:
            self.__status = status
        else:
            self.__status = "Pending"
            print("Status is invalid.")

    # Behaviour: the only way __status can become "Processed"
    def processed(self):
        self.__status = "Processed"
        print("Transaction processed successfully")

    # Behaviour: the only way __status can become "Cancelled"
    def cancelled(self):
        self.__status = "Cancelled"
        print("Transaction cancelled successfully")

    # Setter: desc is the only field editable after creation, validated the same as the constructor
    def set_desc(self, new_desc):
        if isinstance(new_desc, str):
            self.__desc = new_desc
            print("Description updated")
        else:
            print("Description is invalid. Description not changed.")

     # Getters — read-only access to every private attribute
    def get_desc(self):
        return self.__desc

    def get_identifier(self):
        return self.__identifier

    # Setter: transaction_type is editable after creation
    def set_transaction_type(self, new_type):
        if isinstance(new_type, str):
            self.__transaction_type = new_type
        else:
            print("Transaction type is invalid. Type not changed.")

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount
    
    # No setter for status — it only changes via processed()/cancelled() above
    def get_status(self):
        return self.__status

    # Human-readable string, e.g. for print(transaction)
    def __str__(self):
        return (f"Identifier = {self.__identifier}, Type = {self.__transaction_type}, "
                f"Amount = {self.__amount}, Description = \"{self.__desc}\", "
                f"Status = {self.__status}")
    # Developer-facing representation, e.g. for repr(transaction)
    def __repr__(self):
        return (f"Transaction: identifier={self.__identifier}, "
                f"transaction_type={self.__transaction_type}, amount={self.__amount}, "
                f"desc={self.__desc}, status={self.__status}")
