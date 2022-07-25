import requests


def dollar_Consult():
    connection_string = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    price = connection_string.json()
    dollar = round(float(price['USD']['bid']), 2)
    dollar_time = price['USD']['create_date']

    return dollar, dollar_time