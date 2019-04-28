

class Account:

	def __init__(self, sql_adapter):
		self.sql_adapter = sql_adapter
		self.account_info = sql_adapter.load_account_info()

	def buy(self, buy_order):
		pass

	def sell(self, sell_order):
		pass

	def reset(self):
		pass