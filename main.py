# importing the requests library
import requests
from requests import *
import matplotlib.pyplot as plt
URL = "https://digital.iservices.rte-france.com/token/oauth/ "

r = requests.post(URL, headers={"Authorization": "Basic ZDJhMWEyZDctN2E0My00MmQ2LWFhMWMtOThiN2IzMDM0N2NiOjk3MTJmNWRjLTEwZTAtNDRmZi05NDNjLWNhMmMxNTJhYjc1Mw=="})
print(r.json())
print(r.json()['access_token'])
token = r.json()['access_token']

gen = requests.get("https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_production_type", headers={"Authorization": "Bearer "+ token})
#print(gen.json())
#print(gen.json()['actual_generations_per_production_type'][7]['values'][0])
for i in range(0, len(gen.json()['actual_generations_per_production_type'])):
    for j in range(0, len(gen.json()['actual_generations_per_production_type'][i]['values'])):
        print(gen.json()['actual_generations_per_production_type'][i]['production_type'] + " " + str(gen.json()['actual_generations_per_production_type'][i]['values'][j]['value']) + " " + gen.json()['actual_generations_per_production_type'][i]['values'][j]['start_date'])
