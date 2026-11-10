class Transaction:
    """The Transaction class is responsible for representing a single
    transaction and for tracking whether it is still pending, has been
    processed or was cancelled.

    Transaction does not manage the account that holds it, the client who
    owns that account, or branch operations; that responsibility belongs to
    the Account, Client and Branch classes respectively."""

    def __init__(self, identifier, transaction_type,
                 amount, desc, status="Pending"):

        # The identifier must be a positive non-bool number so
        # every account can be told apart.
        if isinstance(identifier, int) and not isinstance(
                identifier, bool) and identifier > 0:
            self.__identifier = identifier
        else:
            self.__identifier = 0
            print("Identifier is invalid.")

        # The type must be a string so it can be compared with labels
        # such as "Deposit" when the history is filtered.
        if isinstance(transaction_type, str):
            self.__transaction_type = transaction_type
        else:
            self.__transaction_type = "No Type"
            print("Transaction type is invalid.")

        # The amount must be a positive (or 0) non-bool number because a
        # negative amount would make the account balance meaningless.
        if isinstance(amount, (int, float)) and not isinstance(
                amount, bool) and amount >= 0:
            self.__amount = amount
        else:
            self.__amount = 0
            print("Amount is invalid.")

        # The description must be a string so it can be printed as readable
        # text.
        if isinstance(desc, str):
            self.__desc = desc
        else:
            self.__desc = "No Description"
            print("Description is invalid.")

        # The status must be one of the three allowed states so a transaction
        # can never end up in a state the rest of the program doesn't expect.
        if isinstance(status, str) and status in [
                "Pending", "Processed", "Cancelled"]:
            self.__status = status
        else:
            self.__status = "Pending"
            print("Status is invalid.")

    @property
    def desc(self):
        return self.__desc

    @property
    def identifier(self):
        return self.__identifier

    @property
    def transaction_type(self):
        return self.__transaction_type

    @property
    def amount(self):
        return self.__amount

    @property
    def status(self):
        return self.__status

    # Processed is the only way __status can become "Processed", and only from
    # "Pending", so a cancelled transaction can't be processed afterwards.
    def processed(self):
        if self.__status == "Pending":
            self.__status = "Processed"
            print("Transaction processed successfully")

    # Cancelled is the only way __status can become "Cancelled", and only from
    # "Pending", so a processed transaction can't be undone afterwards.
    def cancelled(self):
        if self.__status == "Pending":
            self.__status = "Cancelled"
            print("Transaction cancelled successfully")

    # Set_desc changes the description,
    # but only to a string so it stays printable.
    def set_desc(self, new_desc):
        if isinstance(new_desc, str):
            self.__desc = new_desc
            print("Description updated")
        else:
            print("Description is invalid. Description not changed.")

    # Set_transaction_type changes the type, but only to a string so it can
    # still be matched when the history is filtered.
    def set_transaction_type(self, new_type):
        if isinstance(new_type, str):
            self.__transaction_type = new_type
        else:
            print("Transaction type is invalid. Type not changed.")

    # __str__ gives a readable sentence for users who print a transaction.
    def __str__(self):
        return (f"Identifier is {self.__identifier},"
                f"Type is {self.__transaction_type}, "
                f"Amount is {
            self.__amount}, Description is \"{
            self.__desc}\", "
            f"Status is {self.__status}")

    # __repr__ gives an unambiguous line showing every attribute, which is
    # what a programmer needs when debugging.
    def __repr__(self):
        return (f"Transaction: identifier={self.__identifier}, "
                f"transaction_type={
            self.__transaction_type}, amount={
            self.__amount}, "
            f"desc={self.__desc}, status={self.__status}")
