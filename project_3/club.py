from country import Country


class Club:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return self.name
