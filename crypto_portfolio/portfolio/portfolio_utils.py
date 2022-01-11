'''File for utility functions related to data from external API'''

import base64
from io import BytesIO
import matplotlib.pyplot as plt
import requests
import pandas as pd
import numpy as np
from datetime import datetime
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
def coin_request_daily(coin):
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=1'
    response = requests.get(url)
    status_code = response.status_code


    if status_code != 200:
        raise Exception(f"CoinGecko API call failed with status code: {status_code}")
    return response.json()

def total_balance(assets, coin):
    balance = [[], []]

    data = coin_request_30d(coin)
    assets_dates_unix = [[], []]
    for asset in assets:
        assets_dates_unix[0].append(asset)
        assets_dates_unix[1].append(asset.date.timestamp()*1000.0)

    assets_dates_unix[1][0] = datetime(2021,12,15,0,0).timestamp()*1000.0 # for testing

    for el in data['prices']: #el[0] - timestamp el[1] - price
        balance[0].append(1)#float(el[0]))
        balance[1].append(0.)
        for i in range(len(assets_dates_unix[1])):
            if (assets_dates_unix[1][i] <= float(el[0])):
                balance[1][-1] += 1#float(assets_dates_unix[0][i].amount) * float(el[1])

    #return [[], []]
    return balance #[[x], [y]] - x - timestamps, y - balace

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
    dataset = pd.DataFrame.from_dict(coin_request(coin))
    # dataset.drop(dataset.tail(1).index,inplace=True) # Potential problem - same date, 2 values
    dataset = dataset.drop(columns=['market_caps', 'total_volumes'])
    days = 7
    for id in dataset.index:
        dataset.loc[id, 'Date'] = datetime.fromtimestamp(int(dataset.loc[id, 'prices'][0]/1000 + days * 24 * 60 * 60))
        dataset.loc[id, 'prices'] = dataset.loc[id, 'prices'][1]
    dataset['Prediction'] = dataset[['prices']].shift(-days)
    X = np.array(dataset.drop(columns=['Prediction', 'Date'], axis = 1))[:-days]
    y = np.array(dataset['Prediction'])[:-days]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.01)
    x_pred = dataset.drop(columns=['Prediction', 'Date'], axis = 1)[:-days]
    x_pred = x_pred.tail(days)
    x_pred = np.array(x_pred)
    lr = LinearRegression().fit(x_train,y_train)
    y_lrp = lr.predict(x_pred)
    return pd.to_datetime(dataset.Date, format='%Y-%m-%d').tail(2 * days).values, dataset.prices.tail(days), y_lrp

def get_graph():
    logging.warning("get_graph")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, type=0):
    #logging.warning("get_plot")
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.xlabel('Date')
    plt.ylabel(f'Price USD($)')
    if type != 0:
        plt.plot((x[0])[:len(x[0])//2], x[1], label='Previous prices')
        plt.plot((x[0])[len(x[0])//2:], x[2], label='Predicted prices')
        plt.legend()
    else:
        plt.plot(x)
    plt.grid()
    plt.tight_layout()
    graph = get_graph()
    return graph


def add_data(user_assets, data):
    NData = []
    for asset in user_assets.all():
        for elem in data:
            if asset.coin_id == elem['id']:
                history = coin_request_daily(elem['id'])
                dictionary = {}
                dictionary['id'] = asset.coin_id
                dictionary['name'] = asset.name
                dictionary['amount'] = asset.amount
                dictionary['purchase_price'] = asset.price
                dictionary['img'] = elem['image']
                dictionary['price'] = float(str(round(elem['current_price'],4)))
                dictionary['24h'] = float(str(round((history['prices'][0][1] - dictionary['price'])*100/dictionary['purchase_price'],4)))
                dictionary['profit'] = float(str(round(dictionary['price'] - dictionary['purchase_price'],4)))
                NData.append(dictionary)
    return NData

def get_balance_plot(balance):
    x = balance[0]
    y = balance[1]

    plt.plot(x, y)
    graph = get_graph()
    return graph

