from abc import ABC, abstractmethod

from country import Country


class Person(ABC):
    """The shared idea of a person in the game. It is abstract because
    only a specific kind of person (a player or a manager) is ever created."""

    # Players and managers both use this rating when theirs is invalid or
    # missing, so it is stored once here instead of in each class.
    DEFAULT_RATING = 50

    def __init__(self, name, surname, age, nationality):
        # The name and surname must be strings, otherwise defaults are used
        # so the person can still be created.
        if isinstance(name, str):
            self.name = name
        else:
            self.name = "No Name"
            print("Name is invalid.")

        if isinstance(surname, str):
            self.surname = surname
        else:
            self.surname = "No Surname"
            print("Surname is invalid.")

        # Age must be a positive whole number. Bool is rejected.
        if isinstance(age, int) and not isinstance(age, bool) and age > 0:
            self.age = age
        else:
            self.age = 0
            print("Age is invalid.")

        # The nationality must be a Country object so every person is linked
        # to a real country or to nothing at all.
        if isinstance(nationality, Country):
            self.nationality = nationality
        else:
            self.nationality = None
            print("Nationality is invalid.")

    # Every kind of person describes their own role in the game.
    @abstractmethod
    def role(self):
        # There is nothing to do here because Person has no role of its own.
        # Each subclass must override this, or it cannot be created.
        pass

    def __str__(self):
        # Subclasses call this with super() and add their own details, so the
        # shared wording is only written once.
        return f"{self.name} {self.surname} ({self.age})"
