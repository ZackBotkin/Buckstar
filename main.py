import pyodbc
from sql_adapter import SqlAdapter
from account import Account


conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-C5KASSO;'
    'Database=Test;'
    'Trusted_Connection=yes;'
)




def main():

    cursor = conn.cursor()
    sql_adapter = SqlAdapter(cursor)
    account = Account(sql_adapter)

    for item in account.account_info:
        print(item)



if __name__ == '__main__':
    main()
