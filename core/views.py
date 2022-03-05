from django.shortcuts import render
import requests
from decouple import config

def index(request):
    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
    
    headers = {
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
        'x-rapidapi-key': config("rapidapikey")
        }
    
    response = requests.request("GET", url, headers=headers).json()
    data = response['data']
    update = data['last_update']
    confirmed = data['confirmed']
    recovered = data['confirmed_diff']
    deaths = data['deaths']
    active = data['active']
    fatality = data['fatality_rate']

    context = {
        'update':update, 'confirmed':confirmed, 'recovered':recovered, 'deaths':deaths, 'active':active, 'fatality':fatality
    }
    print(data)
    return render(request, 'index.html', context)
