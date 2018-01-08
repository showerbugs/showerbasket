import requests
import hmac
import time
import json
import base64
import hashlib

from config import PERSONAL_API_ACCESS_TOKEN
from config import PERSONAL_API_SECRET_KEY
from config import COINONE_API_SERVER

def get_signature(encoded_payload, secret_key):
    signature = hmac.new(secret_key, encoded_payload, hashlib.sha512)
    return signature.hexdigest()

def get_encoded_payload(payload):
    dumped_json = json.dumps(payload)
    return base64.b64encode(dumped_json.encode('utf-8'))

def get_headers(payload):
    encoded_secret_key = base64.b64encode(PERSONAL_API_SECRET_KEY.upper().encode('utf-8'))
    encoded_payload = get_encoded_payload(payload)
    return {
        'Content-type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': get_signature(encoded_payload, PERSONAL_API_SECRET_KEY.upper().encode('utf-8'))}

def retrieve_currency(currency):
    url = COINONE_API_SERVER + '/ticker'
    payload = {'currency':currency}
    response = requests.get(url, params=payload)
    return response.json()

def retrieve_account_balance():
    url = COINONE_API_SERVER + '/v2/account/balance'
    payload = {
        'access_token': PERSONAL_API_ACCESS_TOKEN,
        'nonce': int(time.time() * 1000)
    }
    response = requests.post(url, headers=get_headers(payload), data=payload)
    result = response.json()
    return result

    

    