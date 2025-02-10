# this code snippet is from the following official documentation:
# https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/python-oauth-token.html
# however, it does not work for the following error, despite it is installed:
# ModuleNotFoundError: No module named 'requests_oauthlib'

# the revised code as follows work fine
import requests, os, configparser, oauthlib.oauth1, json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# get credentials from a local saved properties file
credentials = os.path.join(os.path.expanduser('~'), '.here', 'credentials.properties')
config = configparser.ConfigParser()
with open(credentials, 'r') as f:
    config_string = '[credentials]\n' + f.read()
try:
    config.read_string(config_string)
except AttributeError:
    import StringIO
    buf = StringIO.StringIO(config_string)
    config.readfp(buf)
access_key_id = config.get('credentials', 'here.access.key.id')
access_key_secret = config.get('credentials', 'here.access.key.secret')
endpoint_url = config.get('credentials', 'here.token.endpoint.url')

# generate the token
client = oauthlib.oauth1.Client(access_key_id, access_key_secret)
headers = {'Content-Type':  'application/x-www-form-urlencoded'}
body= {'grant_type': 'client_credentials','expires_in': '86400'}
url, headers, body = client.sign(endpoint_url, http_method='POST', headers=headers, body=body)
data = urlencode(body)
req = Request(url, data=data.encode(), headers=headers)
res = urlopen(req)
body = json.loads(res.read())
access_token = body['access_token']

# testing the token with a search request
s = requests.Session()
s.headers = {'Authorization': f"Bearer {access_token}",
             'Content-Type': 'text/plain'}

params = dict(at='52.5228,13.412', q='restaurant', limit=1)
r = s.get('https://discover.search.hereapi.com/v1/discover', params=params)
print(r.json())
