import requests

BASE_URL = 'https://api.quavergame.com/v1/'

def getuser_full(id):
    attach_url = 'users/full/' + str(id)
    result = requests.get(BASE_URL + attach_url).json()
    return(result)

def getgraph(id, mode):
    attach_url = 'users/graph/rank'
    params = {'id':str(id), 'mode':str(mode)}
    result = requests.get(BASE_URL + attach_url, params = params).json()
    return(result)

def getserverstats():
    attach_url = 'stats'
    result = requests.get(BASE_URL + attach_url).json()
    return(result)
