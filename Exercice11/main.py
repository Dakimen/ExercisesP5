"""This file contains exercise 11."""


class NegativeAccountValueError(Exception):
    """Negative Account Value class error.

    Used to display errors related to bank account value dropping below 0.

    Attributes:
    message (string): message to display in case of this error.
    """

    def __init__(self, message):
        """Create an instance of NegativeAccountValueError.

        Args:
        message (string): message to display.
        """
        self.message = message
        super().__init__(self.message)


class BankAccount:
    """Bank account class.

    Used to store holder's name and balance data.

    Attributes:
    account_holder (string): Account holder's identifying value (name or id).
    balance (int or float): Current balance.

    Methods:
    deposit(amount): Add value (int or float) to increase balance.
    withdraw(amount): Withdraw value (int or float) from balance.
    display_balance(amount): Display account holder and balance.
    """

    def __init__(self, account_holder, balance):
        """Create instance of Bank Account.

        Args:
        account_holder (string): account_holder identifier.
        balance (int or float): current balance value.
        """
        if isinstance(balance, (int, float)):
            if balance < 0:
                raise NegativeAccountValueError(
                    "Balance cannot be less than 0."
                    )
            self.account_holder = account_holder
            self.balance = balance
        else:
            raise ValueError("Balance is not an int or float.")

    def deposit(self, amount):
        """Add value (int or float) to increase balance."""
        if isinstance(amount, (int, float)):
            if not amount < 0:
                self.balance = self.balance + amount
            else:
                raise NegativeAccountValueError(
                    "Amount must be a number above 0."
                    )
        else:
            raise ValueError("Desposited amount must be an int or float.")

    def withdraw(self, amount):
        """Withdraw value (int or float) from balance."""
        if isinstance(amount, (int, float)):
            if not amount > self.balance:
                self.balance = self.balance - amount
            else:
                raise NegativeAccountValueError(
                    "Withdrawn amount must not result in a negative balance."
                    )
        else:
            raise ValueError("Amount withdrawn has to be an int or a float.")

    def display_balance(self):
        """Display account holder and balance."""
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Balance: {self.balance}\n")
