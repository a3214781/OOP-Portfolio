class Client:

    # Attributes
    def __init__(self, number, name, email, age):
        self.number = number
        self.name = name
        self.email = email
        self.age = age


    # Behaviors (methods)
    def changeEmail(self, new_email):
        self.email = new_email
        # Add account