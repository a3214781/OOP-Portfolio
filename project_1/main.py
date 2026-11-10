from client import Client
from branch import Branch
from account import Account
from savings_account import SavingsAccount
from everyday_account import EverydayAccount

print("=== Project 1: Finance ===")
print()

# Clients
client_1 = Client(1, "Alessio", "alessio@gmail.com", 19)
client_2 = Client(2, "Jake", "jake@gmail.com", 23)

# Branches
branch_1 = Branch(1, "Head Office", "Adelaide", "+61 431 324 432")
branch_2 = Branch(2, "Regional Hub", "Alice Springs",
                  "+61 432 657 423", "Open")

# Accounts (one of each specialised type)
savings = SavingsAccount(1, "Holiday Fund", 1000, 0.05)
everyday = EverydayAccount(2, "Spending", 2000)

print("--- Properties ---")
print(client_1)
print(f"Client name: {client_1.name}, email: {client_1.email}")
print(
    f"Branch: {
        branch_1.name} in {
            branch_1.suburb} ({
                branch_1.branch_state})")
print(savings)
print(everyday)
print()

print("--- Client holds different account types ---")
client_1.add_account(savings)
client_1.add_account(everyday)
# Duplicate - rejected
client_1.add_account(savings)
# Wrong type - rejected
client_1.add_account("not an account")
for number, account in client_1.accounts.items():
    print(f"  {number}: {account.account_type}")
client_1.preferred_branch = branch_1
print(f"Preferred branch: {client_1.preferred_branch.name}")
print()

print("--- Retrieve an account through the client ---")
retrieved_account = client_1.get_account(1)
print(retrieved_account)
# No such account number
client_1.withdraw_from(99, 50)
retrieved_account.deposit(100)
print()

print("--- Inherited behaviour: deposit ---")
savings.deposit(500)
everyday.deposit(300)
print(f"Savings balance: {savings.balance}")
print(f"Everyday balance: {everyday.balance}")
print()

print("--- Overridden behaviour: withdraw ---")
print("Savings (min balance is", SavingsAccount.MIN_BALANCE, ")")
client_1.withdraw_from(1, 400)    # Valid
client_1.withdraw_from(1, 1500)   # Breaks minimum balance
print("Everyday (max withdrawal is", EverydayAccount.MAX_WITHDRAW, ")")
client_1.withdraw_from(2, 200)   # Valid
client_1.withdraw_from(2, 600)   # Above the limit
print()

print("--- Polymorphism: same call, different rules ---")
# The loop never checks which kind of account it has.
for account in client_1.accounts.values():
    print(f"{account.account_type} withdraw(600):")
    client_1.withdraw_from(account.number, 600)
print()

print("--- Processing the transaction history ---")
print(f"Savings has {savings.transaction_count()} transactions")
print("Deposits only:")
for transaction in savings.transactions_of_type("Deposit"):
    print("  ", transaction)
print("Amounts above 450:")
for transaction in savings.transactions_above(450):
    print("  ", transaction)
print("Full history:")
savings.display_transactions()
print()

print("--- Transaction records (created by the account) ---")
for account in (savings, everyday):
    print(f"{account.account_type} transactions:")
    for transaction in account.transactions:
        print("  ", transaction)
print()

print("--- Invalid operations create no transactions ---")
history_count_before = len(savings.transactions)
savings.deposit(-50)
savings.withdraw("123")
client_1.withdraw_from(1, 999999)
history_count_after = len(savings.transactions)
print(
    f"Transactions before: {history_count_before}, "
    f"after: {history_count_after}")
print()

print("--- isinstance() ---")
for account in (savings, everyday):
    print(f"{type(account).__name__}: is an Account = "
          f"{isinstance(account, Account)}, "
          f"is SavingsAccount = {isinstance(account, SavingsAccount)}, "
          f"is EverydayAccount = {isinstance(account, EverydayAccount)}")
print()

print("--- Interest (SavingsAccount only) ---")
savings.apply_interest()
print()

print("--- Updates ---")
client_2.email = ("jake.new@gmail.com")
print(f"client_2 email: {client_2.email}")
# Invalid - rejected
client_2.email = ("not-an-email.com")
branch_2.update_phone("+61 400 111 222")
print(f"branch_2 phone: {branch_2.phone}")
print()

print("--- repr() ---")
print(repr(client_2))
print(repr(savings))
print(repr(everyday))
print(repr(branch_2))
print(repr(savings.transactions[0]))

print()
print("--- Exceptions ---")

# SavingsAccount: normal use, then a rule break, then carrying on.
print("Savings: normal withdrawal")
client_1.withdraw_from(1, 50)

savings_balance_before = savings.balance
savings_count_before = savings.transaction_count()

print("Savings: withdrawal that breaks the minimum balance")
client_1.withdraw_from(1, 5000)
print(f"Balance unchanged: {savings.balance == savings_balance_before}")
print(f"History unchanged: "
      f"{savings.transaction_count() == savings_count_before}")

print("Savings: the program carries on")
client_1.withdraw_from(1, 20)
print()

# EverydayAccount: the same three steps with its own rule.
print("Everyday: normal withdrawal")
client_1.withdraw_from(2, 50)

everyday_balance_before = everyday.balance
everyday_count_before = everyday.transaction_count()

print("Everyday: withdrawal over the limit")
client_1.withdraw_from(2, 700)
print(f"Balance unchanged: {everyday.balance == everyday_balance_before}")
print(f"History unchanged: "
      f"{everyday.transaction_count() == everyday_count_before}")

print("Everyday: the program carries on")
client_1.withdraw_from(2, 20)
print()

# Client: an account that doesn't exist.
print("Client: account that doesn't exist")
client_1.withdraw_from(99, 50)
print("The program is still running.")
