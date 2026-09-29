class Transaction:
    """Represents a single transaction on an account."""

    def __init__(self, transaction_type, amount, balance_after):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after

    def __str__(self):
        return f"{self.transaction_type:<10} ${self.amount:>8.2f}   (Balance: ${self.balance_after:.2f})"


class BankAccount:
    """A simple bank account that can deposit, withdraw, and show history."""

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount, self.balance))
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append(Transaction("Withdraw", amount, self.balance))
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print(f"\nTransaction history for {self.owner}:")
        for t in self.transactions:
            print(t)
        print()


# Example usage
if __name__ == "__main__":
    account = BankAccount("Jake", balance=100.0)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(1000)
    account.view_transactions()