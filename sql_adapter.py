

class SqlAdapter:

	ACCOUNT_TABLE = 'Test.dbo.Account'

	def __init__(self, cursor):
		self.cursor = cursor


	def load_account_info(self):
		rows = self.cursor.execute(
			'SELECT * FROM %s' % self.ACCOUNT_TABLE
		)
		return rows