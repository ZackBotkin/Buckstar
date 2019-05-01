


class MockSqlAdapter:

	def __init__(self, accounts, portfolios):
		self.accounts = accounts
		self.portfolios = portfolios

	def load_account_info(self, account_name):
		return accounts[account_name]

	def load_portfolios(self, account_name):
		return accounts[account_name]

	def buy_initial(self, account_name):
		pass