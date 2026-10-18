from country import Country
from club import Club


class Person:
    def __init__(self, name, surname, age, nationality):
        if isinstance(name, str):
            self.name = name
        if isinstance(surname, str):
            self.surname = surname
        if isinstance(age, int) and not isinstance(age, bool):
            self.age = age
        if isinstance(nationality, Country):
            self.nationality = nationality

    def __str__(self):
        return f"{self.name} {self.surname} ({self.age})"
