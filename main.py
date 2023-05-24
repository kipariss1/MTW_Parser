import requests
from bs4 import BeautifulSoup
import re

url = 'https://aviationweather-bldr.ncep.noaa.gov/sigmet/intl?hazard=mtw&loc=all'
my_html = requests.get(url)
my_html_text = my_html.text
soup = BeautifulSoup(my_html_text, 'html.parser')

sigmet_group = soup.find('pre')

sigmet_tags = sigmet_group.find_all('br')

for sigmet_text in sigmet_tags:
    print(sigmet_text.previous)
    location = r'WI\s(.+)\n'
    matches = re.search(location, sigmet_text.previous)
    location_text = matches.group(1)
    print('Location: ', location_text + '\n')




