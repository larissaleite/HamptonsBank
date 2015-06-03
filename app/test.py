import unittest, views, json

class FlaskTestCase(unittest.TestCase):

	def setUp(self):
		views.app.config['TESTING'] = True
		self.app = views.app.test_client()

	def test_index(self):
		rv = self.app.get('/')
		assert 'Hamptons Bank' in rv.data

	def test_credit(self):

		self.app.get('/')

		url = '/credit'
		data = {'amount': 20, 'account': 1}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		assert 'Deposit of 20 to account 1. Bonus of ' + str(20/3) in response.data

	def test_valid_debit(self):

		self.app.get('/')

		url = '/debit'
		data = {'amount': 20, 'account': 1}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		assert 'Withdraw of 20 from account 1' in response.data

	def test_invalid_debit(self):

		self.app.get('/')

		url = '/debit'
		data = {'amount': 199, 'account': 1}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		assert 'Not possible to withdraw this amount from this account. Minimum balance is R$2,00' in response.data

	def test_bonus(self):

		self.app.get('/')

		url = '/credit'
		data = {'amount': 18, 'account': 1}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		url = '/bonus'
		data = {'account': 1}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		assert 'Bonus balance: 6. Continue using our services to accumulate bonus.' in response.data

	def test_balance(self):

		self.app.get('/')

		url = '/balance'
		data = {'account': 1}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		assert '200' in response.data

	def test_transfer(self):

		self.app.get('/')

		url = '/transfer'
		data = {'account_to': 1, 'account_from' : 2, 'amount' : 50}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		assert "Transfer of 50 to account 1" in response.data

	def test_credit_savings(self):
		self.app.get('/')

		url = '/credit_savings'
		data = {'account': 1, 'amount' : 50}
		headers = {'Content-Type': 'application/json'}

		response = self.app.post(url, data=json.dumps(data), headers=headers)

		assert "Successfully deposited 50 to savings account 1" in response.data

if __name__ == '__main__':
    unittest.main()