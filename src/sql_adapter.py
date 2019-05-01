import json
import pyodbc


class SqlAdapter:

	DFEFAULT_CONF_FILE = 'config.json'
	ACCOUNT_TABLE = 'Test.dbo.Account'
	PORTFOLIO_TABLE = 'Test.dbo.Portfolio'

	def __init__(self, conf_file=None):

		if conf_file is None:
			conf_file = self.DFEFAULT_CONF_FILE

		with open(conf_file) as f:
			data = json.load(f)

		self.conn = pyodbc.connect(
    		'Driver=%s;Server=%s;Database=%s;Trusted_Connection=%s;' %
    		(
    			data["Driver"],
    			data["Server"],
    			data["Database"],
    			data["Trusted_Connection"]
    		)
		)

		self.cursor = self.conn.cursor()


	def load_account_data(self, account_name):
		account_info = self.cursor.execute(
			'SELECT * FROM %s WHERE AccountName=\'%s\'' %
			(self.ACCOUNT_TABLE, account_name)
		)
		return account_info.fetchone()

	def load_portfolio_data(self, account_name):
		raw_portfolio = self.cursor.execute(
			'SELECT Symbol,Quantity FROM %s WHERE AccountName=\'%s\'' %
			(self.PORTFOLIO_TABLE, account_name)
		)
		portfolio = {}
		for row in raw_portfolio:
			if (row[0] not in portfolio):
				portfolio[row[0]] = row[1]

		return portfolio


	def buy_initial(self, account_name, quantity, symbol):
		self.cursor.execute(
			"INSERT INTO %s (AccountName, Symbol, Quantity) VALUES (\'%s\',\'%s\',%d)" %
			(self.PORTFOLIO_TABLE, account_name, str(symbol), int(quantity))
		)
		self.conn.commit()

	def buy_more(self, account_name, quantity, symbol):
		self.cursor.execute(
			"UPDATE %s SET Symbol=\'%s\',Quantity=%d WHERE AccountName=\'%s\'" %
			(self.PORTFOLIO_TABLE, symbol, int(quantity), account_name)
		)
		self.conn.commit()

	def update_account(self, account_name, new_balance):
		self.cursor.execute(
			"UPDATE %s SET AccountBalance=%d WHERE AccountName=\'%s\'" %
			(self.ACCOUNT_TABLE, new_balance, account_name)
		)
		self.conn.commit()