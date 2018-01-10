import pytest

from marketcap import MarketCap


@pytest.fixture(scope='session')
def marketcap():
    return MarketCap()
