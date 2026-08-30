class Transaction:
    """The Transaction class is responsible for representing a transaction 
    of the client through (identifier, transaction_type, amount, desc, status), 
    for managing which Transactions are processed if any.

    Transaction does not manage recipient and giver, or branch operations directly,
    that responsibility belongs to the Account, Client, and Branch classes respectively."""

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

    # Getters
    def get_desc(self):
        return self.__desc

    def get_identifier(self):
        return self.__identifier

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    # processed: the only way __status can become "Processed"
    def processed(self):
        self.__status = "Processed"
        print("Transaction processed successfully")

    # cancelled: the only way __status can become "Cancelled"
    def cancelled(self):
        self.__status = "Cancelled"
        print("Transaction cancelled successfully")

    # Setters: set_desc: desc is one of only 2 field editable after creation and is validated the same as the constructor
    def set_desc(self, new_desc):
        if isinstance(new_desc, str):
            self.__desc = new_desc
            print("Description updated")
        else:
            print("Description is invalid. Description not changed.")

    # set_transaction_type: transaction_type is editable after creation if new_type is a str
    def set_transaction_type(self, new_type):
        if isinstance(new_type, str):
            self.__transaction_type = new_type
        else:
            print("Transaction type is invalid. Type not changed.")

    # Human-readable string
    def __str__(self):
        return (f"Identifier = {self.__identifier}, Type = {self.__transaction_type}, "
                f"Amount = {self.__amount}, Description = \"{self.__desc}\", "
                f"Status = {self.__status}")
    # Developer-facing representation

    def __repr__(self):
        return (f"Transaction: identifier={self.__identifier}, "
                f"transaction_type={self.__transaction_type}, amount={self.__amount}, "
                f"desc={self.__desc}, status={self.__status}")
