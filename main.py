# importing the requests library
import requests
from requests import *
URL = "https://digital.iservices.rte-france.com/token/oauth/ "

r = requests.post(URL, headers={"Authorization": "Basic ZDJhMWEyZDctN2E0My00MmQ2LWFhMWMtOThiN2IzMDM0N2NiOjk3MTJmNWRjLTEwZTAtNDRmZi05NDNjLWNhMmMxNTJhYjc1Mw=="})
print(r.json())
print(r.json()['access_token'])
token = r.json()['access_token']
