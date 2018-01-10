import json
import hmac
import hashlib
import base64

from config import config


class API:
    def __init__(self):
        self.root = config.coinone.root
        self.version = config.coinone.version
        self.base = f'{self.root}/{self.version}'

        self.access_token = config.coinone.access_token
        self.secret_key = config.coinone.secret_key

    def _header(self, payload):
        payload = self._encoded_payload(payload)
        signature = self._signature(payload)
        header = {
            'Content-type': 'application/json',
            'X-COINONE-PAYLOAD': payload,
            'X-COINONE-SIGNATURE': signature,
        }
        return header

    def _encoded_payload(self, payload):
        dumped_payload = json.dumps(payload)
        encoded_payload = base64.b64encode(dumped_payload.encode('utf-8'))
        return encoded_payload

    def _signature(self, payload):
        encoded_secret_key = self.secret_key.upper().encode('utf-8')
        signature = hmac.new(
            encoded_secret_key, payload, hashlib.sha512)
        return signature.hexdigest()
