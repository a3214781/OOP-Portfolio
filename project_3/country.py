class Country:
    """A country that people, clubs and leagues belong to."""

    def __init__(self, name):
        # The name must be a string, otherwise a default is used so the
        # country can still be created.
        if isinstance(name, str):
            self.name = name
        else:
            self.name = "No Name"
            print("Country name is invalid.")

    def __str__(self):
        # Only the name is returned so a country prints cleanly inside other
        # sentences, like "a 31 year old from [country_name]".
        return self.name
