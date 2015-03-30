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
	account_1 = Account(1, 200, 0)
	account_2 = Account(2, 250, 0)
	account_3 = Account(3, 100, 0)

	global accounts
	accounts = [account_1, account_2, account_3]

	return render_template('index.html', accounts=accounts)

@app.route('/debit', methods=['POST'])
def debit_account():
	bank = Bank()

	withdrawCommand = WithdrawCommand(find_account(request.json["account"]), int(request.json["amount"]))
	bank.execute(withdrawCommand)

	logging.debug("Debit operation")
	message = "Withdraw of " + str(request.json["amount"]) + " to account "+str(request.json["account"])
	return message

@app.route('/credit', methods=['POST'])
def credit_account():
	bank = Bank()

	depositCommand = DepositCommand(find_account(request.json["account"]), int(request.json["amount"]))
	bank.execute(depositCommand)

	logging.debug("Credit operation")
	message = "Deposit of " + str(request.json["amount"]) + " to account "+str(request.json["account"])
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
	return ""

if __name__ == '__main__':
	app.secret_key = 'secret key'
	app.run(debug=True)