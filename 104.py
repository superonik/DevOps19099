import requests

responce = requests.get('https://en.wikipedia.org/wiki/Main_Page')
if responce.status_code == 200:
    print('Page loaded successfully')
