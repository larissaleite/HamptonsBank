# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, make_response, request, flash
from account import *
from bank import *
from services import *
import logging

accounts = []
  
app = Flask(__name__)

def find_account(id):
	for account in accounts:
		if account.id == id:
			return account

@app.route('/', methods = ['GET'])
def home():
	account_1 = Account(1, 200, 0, 0)
	account_2 = Account(2, 250, 0, 0)
	account_3 = Account(3, 100, 0, 0)

	global accounts
	accounts = [account_1, account_2, account_3]

	return render_template('index.html', accounts=accounts)

@app.route('/debit', methods=['POST'])
def debit_account():
	bank = Bank()

	balanceCommand = BalanceCommand(find_account(request.json["account"]))
	balance = bank.execute(balanceCommand)

	amount = int(request.json["amount"])

	if (balance-amount < 2):
		message = "Not possible to withdraw this amount from this account. Minimum balance is R$2,00"
	else:	
		message = "Withdraw of " + str(request.json["amount"]) + " to account "+str(request.json["account"])

		withdrawCommand = WithdrawCommand(find_account(request.json["account"]), amount)
		bank.execute(withdrawCommand)

	logging.debug("Debit operation")
	return message

@app.route('/credit', methods=['POST'])
def credit_account():
	bank = Bank()

	amount = int(request.json["amount"])
	depositCommand = DepositCommand(find_account(request.json["account"]), amount)
	bank.execute(depositCommand)
	bonus = amount/3

	logging.debug("Credit operation")
	message = "Deposit of " + str(request.json["amount"]) + " to account "+str(request.json["account"])+". Bonus of "+ str(bonus) +" credited."
	return message

@app.route('/balance', methods=['POST'])
def balance_account():
	bank = Bank()

	balanceCommand = BalanceCommand(find_account(request.json["account"]))
	balance = bank.execute(balanceCommand)

	logging.debug("Balance operation")
	return str(balance)

@app.route('/transfer', methods=['POST'])
def transfer():
	bank = Bank()

	print request.json["account_to"]
	transferCommand = TransferCommand(find_account(request.json["account_from"]), find_account(int(request.json["account_to"])), int(request.json["amount"]))
	bank.execute(transferCommand)

	logging.debug("Transfer operation")
	message = "Transfer of " + str(request.json["amount"]) + " to account "+str(request.json["account_to"])
	return message

@app.route('/bonus', methods=['POST'])
def bonus():
	bank = Bank()

	bonusCommand = BonusCommand(find_account(request.json["account"]))
	bonus = bank.execute(bonusCommand)

	message = "Bonus balance: "+str(bonus)+". Continue using our services to accumulate bonus."
	return message

@app.route('/credit_savings', methods=['POST'])
def credit_savings():
	bank = Bank()

	amount = int(request.json["amount"])
	depositSavingsCommand = DepositSavingsCommand(find_account(request.json["account"]), amount)
	bank.execute(depositSavingsCommand)

	logging.debug("Credit savings operation")
	message = "Successfully deposited " + str(request.json["amount"]) + " to savings account "+str(request.json["account"])
	return message

if __name__ == '__main__':
	app.secret_key = 'secret key'
	#app.run(debug=True)
	port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)