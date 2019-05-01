
from src.portfolio import Portfolio

class Account:

	def __init__(
		self,
		account_info= None,
		portfolio=None,
		data_source=None,
		name= 'ZackBot'
	):

		self.name = name
		self.data_source = data_source

		if account_info is None:
			if self.data_source is None:
				raise Exception('Need a data source if no account info passed in')
			else:
				self.account_info = self.data_source.load_account_data(self.name)
		else:
			self.account_info = account_info

		if portfolio is None:
			if self.data_source is None:
				raise Exception('Need a data source if no portfolio provided')
			else:
				self.portfolio = Portfolio(self.name, self.data_source)
		else:
			self.portfolio = portfolio


	def _can_buy(self, order):
		return True

	def buy(self, order):
		if self._can_buy(order):
			self.portfolio.update(order)
		else:
			raise Exception('Invalid buy order')

	def _can_sell(self, order):
		return True

	def sell(self, order):
		if self._can_sell(order):
			self.portfolio.update(order)
		else:
			raise Exception('Invalid sell order')