import hmac
from time import time
from functools import partial
from urllib.parse import urlencode
from hashlib import sha512

import requests


class Poloniex:

    public_methods = {
        'returnTicker', 'return24Volume', 'returnOrderBook', 'returnTradeHistory',
        'returnChartData', 'returnCurrencies', 'returnLoanOrders',
    }

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def __getattr__(self, method):
        if method in self.__dict__:
            return self.__dict__[method]
        return partial(self.call, method)

    def call(self, method, **params):
        params.update(command=method)
        if method in self.public_methods:
            return requests.get('https://poloniex.com/public', params=params).json()
        else:
            params.update(nonce=int(time() * 10**3))
            sign = hmac.new(self.secret.encode(), urlencode(params).encode(), sha512).hexdigest()
            headers = {'Key': self.key, 'Sign': sign}
            return requests.post('https://poloniex.com/tradingApi', data=params, headers=headers).json()
