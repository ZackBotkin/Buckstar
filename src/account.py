

class Account:

	def __init__(self, sql_adapter, name='ZackBot'):

		self.sql_adapter = sql_adapter
		self.account_info = sql_adapter.load_account_info(name)

		self.name = self.account_info[0]
		self.balance = self.account_info[1]

		self.portfolio = sql_adapter.load_portfolio(name)


	def commit_transaction(self, order):

		if order.action == 'buy':
			## TODO : need to look up cost and make sure it doesnt exceeed
			## liquid assets in portfolio
			self.sql_adapter.buy_order(order.action, order.quantity)

		elif order.action == 'sell':
			if order.symbol not in self.portfolio:
				print(
					"Cannot sell %s. Portfolio does not have this asset!"
					% order.symbol
				)
			elif int(order.quantity) > int(self.portfolio[order.symbol]):
				print(
					"Cannot sell %d shares. Portfolio only has %d shares" %
					(int(order.quantity), int(self.portfolio[order.symbol]))
				)
			else:
				print ("Implement sell")

		else:
			raise Exception('Not a buy or sell')