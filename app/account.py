# Receiver
class Account:

	def __init__(self, id, balance, bonus, savings):
		self.id = id
		self.balance = balance
		self.bonus = bonus
		self.savings = savings

	def withdraw(self, amount):
		self.balance -= amount

	def deposit(self, amount):
		self.balance += amount
		self.bonus += amount/3

	def show_balance(self):
		return self.balance

	def show_bonus(self):
		return self.bonus

	def deposit_savings(self, amount):
		self.savings += amount
