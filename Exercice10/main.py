"""This file contains exercise 10."""


class Person:
    """This is a person.

    Attributes:
    name
    age

    Methods:
    display_details(): display information about this person.
    """

    def __init__(self, name, age):
        """Create instance of a person.

        Args:
        name: person's name.
        age: person's age.
        """
        self.name = name
        self.age = age

    def display_details(self):
        """Display information about this person."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    """This is an Employee.

    Attributes:
    name
    age
    salary

    Methods:
    display_details(): Display this employee's details.
    """

    def __init__(self, name, age, salary):
        """Create instance of an employee.

        Args:
        name: employee's name.
        age: employee's age.
        salary: employee's salary.
        """
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        """Display this employee's details."""
        super().display_details()
        print(f"Salary: {self.salary}")
