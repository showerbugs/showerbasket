class TestAccount:
    def test_balance(self, account):
        result = account.balance()

        assert result['result'] == 'success'
        assert 'krw' in result
        assert 'btc' in result
        assert 'bch' in result
        assert 'btg' in result
        assert 'eth' in result
        assert 'etc' in result
        assert 'qtum' in result
        assert 'xrp' in result
        assert 'iota' in result
        assert 'ltc' in result
