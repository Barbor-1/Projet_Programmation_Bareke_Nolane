# TODO : CHECK TIMEOUT
# TODO : CLEANUP

# # importing the requests library
from socket import timeout
import requests
from requests import *
#import matplotlib.pyplot as plt

from network import RTEauth
from network import APIrequest
from utils import format_time

URL = "https://digital.iservices.rte-france.com/token/oauth/ "
key = "ZDJhMWEyZDctN2E0My00MmQ2LWFhMWMtOThiN2IzMDM0N2NiOjk3MTJmNWRjLTEwZTAtNDRmZi05NDNjLWNhMmMxNTJhYjc1Mw=="

#r = requests.post(URL, headers={"Authorization": "Basic ZDJhMWEyZDctN2E0My00MmQ2LWFhMWMtOThiN2IzMDM0N2NiOjk3MTJmNWRjLTEwZTAtNDRmZi05NDNjLWNhMmMxNTJhYjc1Mw=="})
#print(r.json())
#print(r.json()['access_token'])
#token = r.json()['access_token']

GENERATION_URL_API = "https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_production_type"

auth = RTEauth(key)
token = auth.getApiKey()
print(token) # DEBUG

GENERATION_API = APIrequest(GENERATION_URL_API, token)
json = GENERATION_API.getJSON()

#gen = requests.get("https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_production_type", headers={"Authorization": "Bearer "+ token})
#print(gen.json())
#print(gen.json()['actual_generations_per_production_type'][7]['values'][0])

begin_time = format_time()
end_time = format_time()

for i in range(0, len(json['actual_generations_per_production_type'])):
    for j in range(0, len(json['actual_generations_per_production_type'][i]['values'])):

        begin_time.formatTime(json['actual_generations_per_production_type'][i]['values'][j]['start_date'])
        end_time.formatTime(json['actual_generations_per_production_type'][i]['values'][j]['end_date'])

        print(json['actual_generations_per_production_type'][i]['production_type'] + " " + str(json['actual_generations_per_production_type'][i]['values'][j]['value']) + " " + str(end_time.getDateTime() - begin_time.getDateTime()))



