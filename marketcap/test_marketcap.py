class TestMarketCap:
    def test_get(self, marketcap):
        ticker_cap = marketcap.get()

        assert(len(ticker_cap) == 100)  # top 100 coins
