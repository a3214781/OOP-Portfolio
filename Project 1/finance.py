class Client:

    # Attributes
    def __init__(self, number, name, email, age):
        self.number = number
        self.name = name
        self.email = email
        self.age = age


    # Behaviors (methods)
    def changeEmail(self, new_email):
        self.email = new_email
        # Add account

class Account:
    
    # Attributes
    def __init__(self, number, account_type, balance, interest_rate):
        self.number = number
        self.account_type = account_type
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("balance = ", self.balance)
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("balance = ", self.balance)
        else:
            print("insufficient funds")
            
    def interest(self):
        self.balance = self.balance+ (self.balance * self.interest_rate)
        print("balance = ", self.balance)
        # Behaviors (methods)
            # Withdraw
            # Deposit
            # Transfer
            
# Client Objects
client_1 = Client(1, "Alessio", "alessio@gmail.com", 19)
client_2 = Client(1, "Jake", "jake@gmail.com", 23)
client_3 = Client(1, "Dave", "dave@gmail.com", 35)

account_1 = Account(1, "savings", 1000, 0.05)
account_2 = Account(1, "spending", 200, 0.01)
account_3 = Account(2, "savings", 10000, 0.05)
account_4 = Account(3, "spending", 2000, 0.01)

# Test (clients)
print("client_1 email: ", client_1.email)
client_1.changeEmail("alessio.fantasia@gmail.com")
print("client_1 new email: ", client_1.email)

print("client_2 email: ", client_2.email)
client_2.changeEmail("jake45@gmail.com")
print("client_2 new email: ", client_2.email)

# Test (account)         
print("account_1 initial balance: ", account_1.balance)
account_1.deposit(537)
account_1.withdraw(230)
account_1.withdraw(10000)
account_1.interest()
print("account_1 final balance: ", account_1.balance)
print("\n")
print("------------------")
print("\n")
print("account_2 initial balance: ", account_2.balance)
account_2.deposit(124)
account_1.withdraw(15)
account_1.interest()
print("account_2 final balance: ", account_2.balance)
