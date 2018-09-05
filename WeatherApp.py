import requests                         #request information from a webpage
from bs4 import BeautifulSoup           #tools to sort through HTML to grab specified data

def spider(api_request):
    url = 'https://api.weather.gov' + str(api_request)
    html_code = requests.get(url)
    plain_text = html_code.text
    soup_obj = BeautifulSoup(plain_text, 'html.parser')
    print(soup_obj)


spider('/alerts/active/area/CA')