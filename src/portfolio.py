import json
from yahoo_fin import stock_info as si


class Portfolio:

	def __init__(self, account_name, data_source):
		self.account_name = account_name
		self.data_source = data_source
		self._load()

	def _load(self):
		self.symbols = self.data_source.load_portfolio_data(self.account_name)

	def _process_buy_order(self, order):

		if order.symbol not in self.symbols:
			self.data_source.buy_initial(self.account_name, order.quantity, order.symbol)
			self.symbols[order.symbol] = order.quantity
		else:
			new_quantity = self.symbols[order.symbol] + order.quantity
			self.data_source.buy_more(
				self.account_name, new_quantity, order.symbol
			)
			self.symbols[order.symbol] = new_quantity

		print("Bought %d shares of %s!" % (order.quantity, order.symbol))
		print("Current total: %d shares of %s" % (self.symbols[order.symbol], order.symbol))

	def _process_sell_order(self, order):
		if order.symbol not in self.symbols:
			raise Exception('Cannot sell %s. Do not own it' % order.symbol)
		elif int(order.quantity) > int(self.symbols[order.symbol]):
			raise Exception(
				'Cannot sell %d shares of %s. Only have= %d' %
				(order.quantity, order.symbol, self.symbols[order.symbol])
			)
		else:
			raise Exception('Sell not implemented!')

	def get_value(self):

		printable_portfolio = []

		for symbol in self.symbols:
			quantity = self.symbols[symbol]
			current_price = si.get_live_price(symbol)
			printable_portfolio.append(
				{
					'symbol' : symbol,
					'quantity' : quantity,
					'current_price' : current_price,
					'total_value' : current_price * quantity
				}
			)
		print (json.dumps(printable_portfolio, indent=4, sort_keys=True))

	def update(self, order):

		if order.action == 'buy':
			self._process_buy_order(order)

		elif order.action == 'sell':
			self._process_sell_order(order)

		else:
			raise Exception('Unrecognized action type %s' % order.action)

