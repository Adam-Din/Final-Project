import requests
import json

#Gets 100 mosrt populous cities from Data USA API.
def get_city_populations():
    pop_list = []
    base_url = 'https://datausa.io/api/data?'
    params = {'drilldowns': 'Place', 'measures': 'Population', 'year':'latest'}
    resp = requests.get(base_url, params)
    resp = json.loads(resp.text)
    for city in resp['data']:
        pop_list.append((city['Place'], city['Population']))
    pop_list_sorted = sorted(pop_list, key = lambda x: x[1], reverse = True)
    return pop_list_sorted[:150]





    



print(get_city_populations())
