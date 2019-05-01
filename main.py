import argparse

from src.order import Order
from src.account import Account
from src.sql_adapter import SqlAdapter


def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "action",
        choices=['buy', 'sell', 'review']
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

    data_source = SqlAdapter()
    account = Account(name= 'ZackBot', data_source= data_source)

    if args.action == 'buy':
        account.buy(Order(args.action, args.symbol, int(args.quantity)))
    elif args.action == 'sell':
        account.sell(Order(args.action, args.symbol, int(args.quantity)))
    elif args.action == 'review':
        account.portfolio.get_value()
    else:
        raise Exception('Unknown action type %s' % args.action)

if __name__ == '__main__':
    main()
