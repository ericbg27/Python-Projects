class Account:

	def __init__(self,owner,balance):

		self.owner = owner
		self.balance = balance

	def print_balance(self):
		print(self.balance)

	def print_owner(self):
		print(self.owner)

	def deposit(self, quantity):
		if(quantity > 0):
			print("Deposit Accepted")
			self.balance += quantity

	def withdraw(self, amount):
		if(self.balance >= amount):
			print("Withdraw Accepted")
			self.balance -= amount
		else:
			print("Funds Unavailable!")

	def __str__(self):
		return "Account owner:\t{}\nAccount balance:\t${}".format(self.owner, self.balance)

acct1 = Account('Jose', 100)

print(acct1)
print("\n")
print(acct1.owner)
print("\n")
print(acct1.balance)
print("\n")
acct1.deposit(50)
print("\n")
acct1.withdraw(75)
print("\n")
acct1.withdraw(500)