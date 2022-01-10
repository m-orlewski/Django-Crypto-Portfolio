'''File for utility functions related to data from external API'''

import base64
from io import BytesIO
import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import logging
from datetime import datetime

def make_request():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    response = requests.get(url)
    status_code = response.status_code

    if status_code != 200:
        raise Exception(f"CoinGecko API call failed with status code: {status_code}")
    
    return response.json()

#Calc functions

def total_balance(assets, coin):
    balance = [[], []]

    data = coin_request_30d(coin)
    assets_dates_unix = [[], []]
    for asset in assets:
        assets_dates_unix[0].append(asset)
        assets_dates_unix[1].append(asset.date.timestamp()*1000)

    assets_dates_unix[1][0] = datetime(2021,12,15,0,0).timestamp()*1000 # for testing

    for el in data['prices']: #el[0] - timestamp el[1] - price
        balance[0].append(el[0])
        balance[1].append(0)
        for i in range(len(assets_dates_unix[1])):
            if (int(assets_dates_unix[1][i]) <= int(el[0])):
                balance[1][-1] += float(assets_dates_unix[0][i].amount) * float(el[1])

    for i in range(len(balance[0])):
        print(balance[0][i], balance[1][i])

    return balance #[[x], [y]] - x - timestamps, y - balace

def add_data(user_asset, data):
    pass

def coin_request_30d(coin):
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=60'
    response = requests.get(url)
    status_code = response.status_code

    if status_code != 200:
        raise Exception(f"CoinGecko API call failed with status code: {status_code}")
    
    return response.json()

def coin_request(coin):
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=max'
    response = requests.get(url)
    status_code = response.status_code

    if status_code != 200:
        raise Exception(f"CoinGecko API call failed with status code: {status_code}")
    
    return response.json()

def get_ml_data(coin):
    #logging.warning("get_ml_data")
    dataset = pd.DataFrame.from_dict(coin_request(coin))
    for id in dataset.index:
        for col in ['prices', 'market_caps', 'total_volumes']:
            dataset.loc[id, col] = dataset.loc[id, col][1]
    dataset = dataset.astype(np.float64, errors = 'raise')
    X = dataset.drop('prices', axis = 1)
    y = dataset['prices']
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=0)
    temp = np.isnan(X_train)
    X_train[temp] = 0
    temp = np.isnan(Y_train)
    Y_train[temp] = 0
    #print('good')
    return dataset['prices']
    

def get_graph():
    #logging.warning("get_graph")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    plt.savefig('test.png')
    return graph

def get_plot(x):
    #logging.warning("get_plot")
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.xlabel('Days')
    plt.ylabel(f'Price USD($)')
    plt.plot(x)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_balance_plot(balance):
    x = balance[0]
    y = balance[1]

    plt.plot(x, y)
    graph = get_graph
    return graph
