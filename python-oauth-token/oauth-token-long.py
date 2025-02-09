# this code snippet is from the following official documentation:
# https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/python-oauth-token.html
# however, it does not work for the following error, despite it is installed:
# ModuleNotFoundError: No module named 'requests_oauthlib'

import requests
from requests_oauthlib import OAuth1

access_key_id = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'

oauth = OAuth1(client_key=access_key_id, client_secret=access_key_secret, signature_type='auth_header')
r = requests.post('https://account.api.here.com/oauth2/token',data=dict(grant_type='client_credentials'), auth=oauth,
                  headers={'Content-Type' : 'application/x-www-form-urlencoded'})

access_token = r.json()['access_token']
print(f'access token generated:\n{access_token}')

s = requests.Session()
s.headers = {'Authorization': f"Bearer {access_token}",
             'Content-Type': 'text/plain'}
 
params = dict(at='52.5228,13.412', q='restaurant', limit=1)
r = s.get('https://discover.search.hereapi.com/v1/discover', params=params)
print(r.json())

