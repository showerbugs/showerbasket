import time

import requests

from api import API


class Account(API):
    def __init__(self):
        super().__init__()
        self.base = f'{self.base}/account'

    def balance(self):
        url = f'{self.base}/balance'
        payload = {
            'access_token': self.access_token,
            'nonce': int(time.time() * 1000),
        }
        header = self._header(payload)

        resp = requests.post(url, headers=header, data=payload)
        result = resp.json()
        return result
