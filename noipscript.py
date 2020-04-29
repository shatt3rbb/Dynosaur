#!/usr/bin/python3

import requests
import base64
import string
import time
from requests.exceptions import ConnectionError

#Input no-ip credentials
username = '' 
password = ''
credential = str(username + ':' + password)

hostname = 'warpgate.ddns.net' #Input your desired no-ip hostname here

encoded_cred = base64.b64encode(credential.encode())
encoded_cred = encoded_cred.decode()

authorize = 'Basic ' + encoded_cred

headers = {'Host': 'dynupdate.no-ip.com',
           'Authorization': authorize,
           'User-Agent': 'Stelios Update Client Raspberry/v0.1 stzaneti@physics.auth.gr'} #Replace the User-Agent with your desired one

while(True):
    try:
        my_ip = requests.get('http://ip.42.pl/raw').text
        url = str('http://dynupdate.no-ip.com/nic/update?hostname=' + hostname + '&myip=' + my_ip)
        r = requests.get(url, headers=headers)
        print(r.text)
        time.sleep(60)
    except(ConnectionError):
        print('Public ip parsing service cannot be reached')
        time.sleep(60)
        continue


