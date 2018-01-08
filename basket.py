import pprint

from api.coinone import Account


account = Account()
pprint.pprint(account.balance())
