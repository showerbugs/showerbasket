import pytest

from api.coinone import Account


@pytest.fixture(scope='session')
def account():
    return Account()
