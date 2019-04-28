import argparse

from order import Order
from account import Account
from sql_adapter import SqlAdapter



def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "action",
        choices=['buy', 'sell']
    )

    parser.add_argument(
        "quantity"
    )

    parser.add_argument(
        "symbol"
    )

    return parser.parse_args()

def main():

    args = get_args()

    sql_adapter = SqlAdapter()
    account = Account(sql_adapter)

    account.commit_transaction(
        Order(
            args.action,
            args.symbol,
            args.quantity
        )
    )


if __name__ == '__main__':
    main()
