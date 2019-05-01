import unittest


from account import Account

class TestAccountMethods(unittest.TestCase):

	def test_buy(self):

		mock_sql_adapter = MockSqlAdapter()

		account = Account()

		self.assertTrue('foo'.upper(), 'FOO')


if __name__ == '__main__':
	unittest.main()