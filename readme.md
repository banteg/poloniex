# poloniex

minimal [poloniex api](https://poloniex.com/support/api/) wrapper

```python
from poloniex import Poloniex
polo = Poloniex('key', 'secret')
polo.buy(currencyPair='BTC_ETH', rate=0.05, amount=100)
```