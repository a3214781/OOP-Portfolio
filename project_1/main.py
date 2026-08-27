from client import Client
from account import Account
from branch import Branch
from transaction import Transaction

# Clients
# FIXED: client numbers were all 1 — now unique
client_1 = Client(1, "Alessio", "alessio@gmail.com", 19)
client_2 = Client(2, "Jake", "jake@gmail.com", 23)
client_3 = Client(3, "Dave", "dave@gmail.com", 35)

# Accounts
# FIXED: account numbers were duplicated (1,1,2,3) — now unique
account_1 = Account(1, "user 1", "savings", 1000, 0.05)
account_2 = Account(2, "expenses", "spending", 200, 0.01)
account_3 = Account(3, "subscription", "savings", 10000, 0.05)
account_4 = Account(4, "holiday", "spending", 2000, 0.01)

# Transactions
transaction_1 = Transaction(1, "Essential", 15.5, "bought lunch")
transaction_2 = Transaction(2, "Lifestyle", 67.8, "new shirt")
transaction_3 = Transaction(3, "Financial", 1500, "rent")

# Branches
branch_1 = Branch(1, "Head Office", "Adelaide", "+61 431 324 432")
branch_2 = Branch(2, "Regional Hub", "Alice Springs", "+61 432 657 423", "Open")
branch_3 = Branch(3, "Coastal Bureau", "Darwin", "+61 433 987 654")

# Demonstrate __str__() on one instance of each class
print(client_1)
print(branch_1)
print(account_1)
print(transaction_1)
# --- Aggregation: Client-Account ---
print("=== Aggregation: Client-Account ===")
client_1.add_account(account_1)
client_1.add_account(account_2)
client_1.add_account(account_1)          # duplicate — rejected
client_1.add_account("not an account")   # wrong type — rejected

print(f"{client_1.get_name()}'s accounts:", client_1.get_accounts())

client_1.remove_account(account_1)
print(f"{client_1.get_name()}'s accounts after removal:", client_1.get_accounts())
print("account_1 still exists:", account_1)

client_1.remove_account(account_3)  # never assigned — rejected
print()

# --- Association: Client-Branch ---
print("=== Association: Client-Branch ===")
client_1.set_preferred_branch(branch_1)
client_2.set_preferred_branch(branch_2)

print(f"{client_1.get_name()}'s preferred branch:", client_1.get_preferred_branch())
print(f"{client_2.get_name()}'s preferred branch:", client_2.get_preferred_branch())

client_1.set_preferred_branch("not a branch")  # wrong type — rejected

client_1.set_preferred_branch(branch_3)
print(f"{client_1.get_name()}'s new preferred branch:", client_1.get_preferred_branch())
print(f"{client_2.get_name()}'s preferred branch (unchanged):", client_2.get_preferred_branch())
print()