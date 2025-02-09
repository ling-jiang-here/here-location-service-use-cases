import requests
api_key = "your_api_key"
latitude, longitude = 45.464664, 9.188540
base_url = f'https://smap.hereapi.com/v8/maps/attributes?apiKey={api_key}&filter=TRAFFIC_SIGN_TYPE=20'
layers = "&layers=TRAFFIC_SIGN_FCn"

for radius in (3000, 5000, 7000, 10000):
    search = f"&in=proximity:{latitude},{longitude};r={radius}"
    url = base_url + search + layers
    r = requests.get(url)
    traffic = len([x for x in r.json()['geometries']])
    print(f"center at ({latitude},{longitude}) with radius {radius}: {traffic} traffic signs")