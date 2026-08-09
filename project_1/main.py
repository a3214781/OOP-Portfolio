from client import Client
from account import Account
from branch import Branch
from transaction import Transaction

# Clients
client_1 = Client(1, "Alessio", "alessio@gmail.com", 19)
client_2 = Client(1, "Jake", "jake@gmail.com", 23)
client_3 = Client(1, "Dave", "dave@gmail.com", 35)

# Accounts
account_1 = Account(1, "savings", 1000, 0.05)
account_2 = Account(1, "spending", 200, 0.01)
account_3 = Account(2, "savings", 10000, 0.05)
account_4 = Account(3, "spending", 2000, 0.01)

# Transactions
trasnaction_1 = Transaction(1, "Essential", 15.5, "bought lunch")
trasnaction_2 = Transaction(2, "Lifestyle", 67.8, "new shirt")
trasnaction_3 = Transaction(3, "Financial", 1500, "rent")

# Branches
branch_1 = Branch(1, "Head Office", "Adelaide", "+61 431 324 432")
branch_2 = Branch(2, "Regional Hub", "Alice Springs", "+61 432 657 423", True)
branch_3 = Branch(3, "Coastal Bureau", "Darwin", "+61 433 987 654")

# Updating Client
print("=== Client UPDATE ===")
print("client_1 email: ", client_1.email)
client_1.changeEmail("alessio.fantasia@gmail.com")
print("client_1 new email: ", client_1.email)
print()

# Updating Account
print("=== Account UPDATE ===")
print("account_1 initial balance: ", account_1.balance)
account_1.deposit(537)
account_1.withdraw(230)
print("account_1 final balance: ", account_1.balance)
print()

# Updating Transactions
print("=== Transaction UPDATE ===")
print(trasnaction_2)
trasnaction_2.processed()
print(trasnaction_2)
print()

# Updating Branch
print("=== Branch UPDATE ===")
print(branch_1)
branch_1.open()
print(branch_1)
print()

