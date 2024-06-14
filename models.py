# models.py

class User:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class USSDSession:
    def __init__(self, user):
        self.user = user
        self.balance = 0
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def recharge(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Recharged: ${amount}")
        return self.balance

    def view_transaction_history(self):
        return self.transaction_history
