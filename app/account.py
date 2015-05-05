# Receiver
class Account:

	def __init__(self, id, balance, bonus):
		self.id = id
		self.balance = balance
		self.bonus = bonus

	def withdraw(self, amount):
		self.balance -= amount

	def deposit(self, amount):
		self.balance += amount
		self.bonus += amount/3

	def show_balance(self):
		return self.balance

	def show_bonus(self):
		return self.bonus