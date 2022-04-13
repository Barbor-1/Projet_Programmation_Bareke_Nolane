import time
import requests
class RTEauth:
    def __init__(self, key):
        self.key = key
        self.timeout = 0
        self.time = time.time()
        self.token = ""
        self.url = "https://digital.iservices.rte-france.com/token/oauth/ "
    def getApiKey(self):
        r = requests.post(self.url, headers={"Authorization": "Basic " + str(self.key)})
        if r.status_code == 200:
            self.token = r.json()['access_token']
            self.timeout = r.json()['expires_in']
            self.time = time.time()
            return self.token
        else:
            raise Exception("Status code is different than 0", r.status_code)
    def timeoutCheck(self):
        if(time.time() < self.time + self.timeout):
            return True
        else:
             return False


