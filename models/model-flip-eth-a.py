#!/usr/bin/env python
import os
import sys
import json
import requests

discount = 0.15

def get_price():
    resp = requests.get('https://api.coingecko.com/api/v3/simple/price', params={'ids': 'ethereum', 'vs_currencies': 'usd'})
    return resp.json()['ethereum']['usd']

for line in sys.stdin:
    signal = json.loads(line)
    if signal['guy'] == os.environ['0x9be74B5ef410BC39A67e71AD01fA5B4F3d2E48A1']:
        continue
    oracle = get_price()
    stance = {'price': oracle * (1 - discount)}
    print(json.dumps(stance), flush=True)