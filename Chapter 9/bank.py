"""
File: bank.py
defines the bank class
"""

from savingsaccount import SavingsAccount
import pickle

class Bank(object):

    def __init__(self, fileName = None):
        """Creates a new dictionary to hold the accounts. If a filename
        is provided, loads the accounts from a file of pickled accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, "rb")
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break

    def __str__(self):
        """Returns the string representation of the entire bank."""
        return '\n'.join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        """Mkaes and returns a key from name and pin."""
        return name + "/" + pin

    def add(self, account):
        """Inserts an account with name and pin as a key."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, oin):
        """Removes an account with name and pin as a key."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns an account with name and pin as a key or
        None if not found."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes interest for each account and returns the total."""
        total = 0.0
        for account in self.accounts.values():
            total += account.computeInterest()
        return Total

    def save(self, fileName = None):
        """Saves pickled accounts to a file. The parameter allows the
        user to change filenames."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()
        
