"""
File: savingsaccount.py
Defines the SavingsAccount Class
"""

class SavingsAccount(object):
    """This class represents a savings account with the owner's name,
    PIN, and balance."""

    RATE = 0.02         #Single rate for all acounts

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string rep."""
        result = 'Name:      ' + self.name + '\n'
        result += 'PIN:      ' + self.pin + '\n'
        result += 'Balance   ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getPin(self):
        """Returns the current PIN."""
        return self.pin

    def getName(self):
        """Returns the current name."""
        return self.name
    
    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount. Returns None if successful, or an
        error message if unsuccessful."""
        if amount < 0:
            return "Amount must be greater than or equal zero."
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest
