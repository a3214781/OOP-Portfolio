from client import Client
from account import Account
from branch import Branch
from transaction import Transaction

# Clients
client_1 = Client(1, "Alessio", "alessio@gmail.com", 19)
client_2 = Client(2, "Jake", "jake@gmail.com", 23)
client_3 = Client(3, "Dave", "dave@gmail.com", 35)

# Accounts
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
branch_2 = Branch(2, "Regional Hub", "Alice Springs",
                  "+61 432 657 423", "Open")
branch_3 = Branch(3, "Coastal Bureau", "Darwin", "+61 433 987 654")

# Demonstrate __str__() on one instance of each class
print(client_1)
print(branch_1)
print(account_1)
print(transaction_1)
print()

# Client-Account
client_1.add_account(account_1)
client_1.add_account(account_2)
client_1.add_account(account_1)          # duplicate — rejected
client_1.add_account("not an account")   # wrong type — rejected

print(f"{client_1.get_name()}'s accounts:", client_1.get_accounts())

client_1.remove_account(account_1)
print(f"{client_1.get_name()}'s accounts after removal:",
      client_1.get_accounts())
print("account_1 still exists:", account_1)

client_1.remove_account(account_3)  # rejected
print()

# Association: Client-Branch
client_1.set_preferred_branch(branch_1)
client_2.set_preferred_branch(branch_2)

print(f"{client_1.get_name()}'s preferred branch:",
      client_1.get_preferred_branch())
print(f"{client_2.get_name()}'s preferred branch:",
      client_2.get_preferred_branch())

client_1.set_preferred_branch("not a branch")  # wrong type — rejected

client_1.set_preferred_branch(branch_3)
print(f"{client_1.get_name()}'s new preferred branch:",
      client_1.get_preferred_branch())
print(f"{client_2.get_name()}'s preferred branch (unchanged):",
      client_2.get_preferred_branch())
print()

# Account operations: (deposit, withdraw, overdraw, invalid values)
print(f"account_1 balance before deposit: {account_1.get_balance()}")
account_1.deposit(500)
print(f"account_1 balance after deposit: {account_1.get_balance()}")

print(f"account_2 balance before withdraw: {account_2.get_balance()}")
account_2.withdraw(50)
print(f"account_2 balance after withdraw: {account_2.get_balance()}")

print(f"account_2 balance before overdraw attempt: {account_2.get_balance()}")
account_2.withdraw(10000)  # insufficient funds — rejected
print(
    f"account_2 balance after overdraw attempt (unchanged): {account_2.get_balance()}")

account_1.deposit(-50)     # invalid amount — rejected
account_1.withdraw("123")  # invalid type — rejected
print()

# Account info update
print(f"account_4 before: {account_4}")
account_4.update_account_info("holiday fund", "savings")
print(f"account_4 after: {account_4}")
account_4.update_account_info(123, "savings")  # not changed - invalid
print()

# Client info update
print(f"client_2 email before: {client_2.get_email()}")
client_2.set_email("jake.new@gmail.com")
print(f"client_2 email after: {client_2.get_email()}")

client_2.set_email("not-an-email.com")  # invalid, no "@" — rejected
print(f"client_2 email unchanged: {client_2.get_email()}")
print()

# Transaction operations
print(f"transaction_1 status before: {transaction_1.get_status()}")
transaction_1.processed()
print(f"transaction_1 status after: {transaction_1.get_status()}")

print(f"transaction_2 status before: {transaction_2.get_status()}")
transaction_2.cancelled()
print(f"transaction_2 status after: {transaction_2.get_status()}")

# Invalid transition
print(
    f"transaction_1 status before second processed() call: {transaction_1.get_status()}")
transaction_1.processed()
print(f"transaction_1 status after: {transaction_1.get_status()}")

transaction_3.set_desc("March rent payment")
print(f"transaction_3 updated description: {transaction_3.get_desc()}")
transaction_3.set_desc(12345)  # invalid — not changed
print()

# Branch operations
print(f"branch_3 status before: {branch_3.get_branch_state()}")
branch_3.opened()
print(f"branch_3 status after: {branch_3.get_branch_state()}")

branch_2.closed()
print(f"branch_2 status after closed(): {branch_2.get_branch_state()}")

print(f"branch_1 phone before: {branch_1.get_phone()}")
branch_1.update_phone("+61 400 111 222")
print(f"branch_1 phone after: {branch_1.get_phone()}")

branch_1.update_phone(12345)  # invalid — not changed
print()

# Branch info update
print(f"branch_2 before: {branch_2}")
branch_2.updateInfo("Regional Hub North", "Alice Springs", "+61 432 000 111")
print(f"branch_2 after: {branch_2}")
print()

# repr() demonstration
print(repr(client_3))
print(repr(account_3))
print(repr(transaction_3))
print(repr(branch_3))
