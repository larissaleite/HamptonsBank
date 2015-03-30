# Receiver
class Account:

	def __init__(self, id, balance):
		self.id = id
		self.balance = balance

	def withdraw(self, amount):
		self.balance -= amount

	def deposit(self, amount):
		self.balance += amount

	def show_balance(self):
		return self.balance