import pprint

from api.coinone import Account
from marketcap import MarketCap


account = Account()
pprint.pprint(account.balance())

marketcap = MarketCap()
pprint.pprint(marketcap.get())
