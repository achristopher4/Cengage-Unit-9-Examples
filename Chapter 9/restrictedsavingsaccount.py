"""
File: restrictedsavingsaccount.py
Defines the RestrictedSavingsAccount class.
"""

from savingsaccount import SavingsAccount

class RestrictedSavingsAccount(SavingsAccount):
    """This class represents a restricted savings account."""

    MAX_WITHDRAWALS = 3

    def __init__(self, name, pin, balance = 0.0):
        """Same attributes as SavingsAccount, but with a counter for
        withdrawasls."""
        SavingsAccount.__init__(self, name, pin, balance)
        self.counter = 0

    def withdraw(self, amount):
        """Restricts number of withdrawaks to MAX_WITHDRAWALS."""
        if self.counter == RestrictedSavingsAccount.MAX_WITHDRAWALS:
            return 'No more withdrawals this month'
        else:
            message = SavingsAccount.withdraw(self, amount)
            if message == None:
                self.counter += 1
            return message

    def resetCounter(self):
        """Resets the withdrawal count."""
        self.counter = 0

    
