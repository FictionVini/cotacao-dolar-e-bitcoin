import requests
import json 


def consulta_contacao(url_api):
    r = requests.get(url_api)    
    if r.status_code == 200:
        return r.json()
    else:
        print('Houve um erro na consulta da api')
    
url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL,BTC-USD'
full_data = consulta_contacao(url)

data = full_data['USDBRL']   #Filtra somente Dol do json
bitcao = full_data['BTCUSD'] #Filtra somente btc do json

name = data['name']
value_high = data['high']
value_low = data['low']
time_stamp = data['create_date']
print(f'A cotação do {name} é {value_high} \n  data_consulta: {time_stamp}')

b_name = bitcao['name']
b_value_high = bitcao['high']
b_time_stamp = bitcao['create_date']
print(f'A cotação do {b_name} é {b_value_high} \n  data_consulta: {b_time_stamp}')
