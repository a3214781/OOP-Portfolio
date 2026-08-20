class Client:

    # Attributes
    def __init__(self, number, name, email, age):
        self.__number = number
        self.__name = name
        self.__email = email
        self.__age = age

    # Behaviors (methods)

    def set_email(self, new_email):
        self.__email = new_email
        # Add account

    def __str__(self):
        return f"Number = {self.__number}, Name = {self.__name}, Email = {self.__email}, Age = {self.__age}"
    # Include the client number, name, and preferred contact method.

    def __repr__(self):
        return f"Client: number={self.__number}, name={self.__name}, email={self.__email}, age={self.__age}"
        # Include enough attribute values to identify the object’s current state.
