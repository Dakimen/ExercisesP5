"""This file contains classes used to display a full name.

MyClass:
Class instance for storing and displaying a full name.

    Args:
    full_name (string): containing a full name

    Methods:
    display_name():
    Display a full name stored in class instance.

OtherClass:
    Class instance for storaing and displaying a full name.
    Args:
    first_name (string): containing a first name
    name (string): containing a last name

    Methods:
    Display a full name by assembling it from first and last name
"""


class MyClass:
    """Class instance for storing and displaying a full name.

    Args:
    full_name (string): containing a full name

    Attributes:
        self.full_name (string): contains an assigned full name.

    Methods:
    display_name():
    Displays a full name stored in class instance.
        Args:
        None
    """

    def __init__(self, full_name):
        """Initiate class instance of MyClass.

        Args:
        full_name (string): a full name.

        Attributes:
        self.full_name (string): contains an assigned full name.
        """
        self.full_name = full_name

    def display_name(self):
        """Display a full name stored in class instance."""
        print("Le nom complet est : ", self.full_name)


class OtherClass:
    """Class instance for storaing and displaying a full name.

    Args:
    first_name (string): containing a first name
    name (string): containing a last name

    Attributes:
        self.first_name (string): contains an assigned first name.
        self.last_name (string): contains an assigned last name.

    Methods:
    display_name():
    Display a full name by assembling it from first and last name,
    stored in class instance.
        Args:
        None
    """

    def __init__(self, first_name, name):
        """Initiate class instance of MyClass.

        Args:
        first_name (string): a first name.
        name (string): a last name.

        Attributes:
        self.first_name (string): contains an assigned first name.
        self.last_name (string): contains an assigned last name.
        """
        self.first_name = first_name
        self.name = name

    def display_name(self):
        """Display a full name."""
        print(f"Nom complet : {self.first_name} {self.name}")
