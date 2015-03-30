class Command:
	def execute(self):
		raise NotImplementedError()

class DepositCommand(Command):

	def __init__(self, account, amount):
		self.account = account
		self.amount = amount

	def execute(self):
		self.account.deposit(self.amount)

class WithdrawCommand(Command):

	def __init__(self, account, amount):
		self.account = account
		self.amount = amount

	def execute(self):
		self.account.withdraw(self.amount)


class BalanceCommand(Command):

	def __init__(self, account):
		self.account = account

	def execute(self):
		return self.account.show_balance()

class TransferCommand(Command):

	def __init__(self, account_from, account_to, amount):
		self.account_from = account_from
		self.account_to = account_to
		self.amount = amount

	def execute(self):
		self.account_from.withdraw(self.amount)
		self.account_to.deposit(self.amount)