'''File for utility functions related to data from external API'''

import requests

def make_request():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    response = requests.get(url)
    status_code = response.status_code

    if status_code != 200:
        raise Exception(f"CoinGecko API call failed with status code: {status_code}")
    
    return response.json()


#Calc functions


def add_data(user_asset, data):
    print()