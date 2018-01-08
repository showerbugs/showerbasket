import api.coinone as coinone_api

def test_retrieve_currency():
    result = coinone_api.retrieve_currency('qtum')
    print(result)
    assert result

def test_balance():
    result = coinone_api.retrieve_account_balance()
    print(result)
    assert result
    