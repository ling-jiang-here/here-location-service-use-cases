# this version is longer, but it works as expected too.

import requests, time, urllib.parse, hmac, hashlib, binascii
from base64 import b64encode

grant_type = 'client_credentials'
oauth_consumer_key = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'
oauth_nonce = str(int(time.time()*1000))
oauth_timestamp = str(int(time.time()))
oauth_signature_method = 'HMAC-SHA256'
oauth_version = '1.0'
url = 'https://account.api.here.com/oauth2/token'

# HMAC-SHA256 hashing algorithm to generate the OAuth signature
def create_signature(secret_key, signature_base_string):
    encoded_string = signature_base_string.encode()
    encoded_key = secret_key.encode()
    temp = hmac.new(encoded_key, encoded_string, hashlib.sha256).hexdigest()
    byte_array = b64encode(binascii.unhexlify(temp))
    return byte_array.decode()

def create_encoded_oauth_signature():
    parameter_string = 'grant_type=' + grant_type + \
        '&oauth_consumer_key=' + oauth_consumer_key + \
        '&oauth_nonce=' + oauth_nonce + \
        '&oauth_signature_method=' + oauth_signature_method + \
        '&oauth_timestamp=' + oauth_timestamp + \
        '&oauth_version=' + oauth_version
    encoded_parameter_string = urllib.parse.quote(parameter_string, safe='')
    encoded_base_string = 'POST&' + urllib.parse.quote(url, safe='') + '&' + encoded_parameter_string

    oauth_signature = create_signature(access_key_secret + '&', encoded_base_string)
    return urllib.parse.quote(oauth_signature, safe='')

body = {'grant_type' : '{}'.format(grant_type)}
authorization = f'OAuth oauth_consumer_key="{oauth_consumer_key}",\
                    oauth_nonce="{oauth_nonce}",\
                    oauth_signature="{create_encoded_oauth_signature()}",\
                    oauth_signature_method="HMAC-SHA256",\
                    oauth_timestamp="{oauth_timestamp}",\
                    oauth_version="1.0"'
headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization' : authorization
          }
response = requests.post(url, data=body, headers=headers)
access_token = response.json()['access_token']
print(access_token)

# perform a Geocoder request to test the generated access token
s = requests.Session()
s.headers = {'Authorization': f"Bearer {access_token}",
             'Content-Type': 'text/plain'}
 
params = dict(at='52.5228,13.412', q='restaurant', limit=1)
r = s.get('https://discover.search.hereapi.com/v1/discover', params=params)
item = r.json()['items'][0]
title = item['title']
address = item['address']['label']
position = f"({item['position']['lat']},{item['position']['lng']})"
print(f'found {title} with address {address} at {position}')