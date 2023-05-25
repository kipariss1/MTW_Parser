import requests
from bs4 import BeautifulSoup
import re

url = 'https://aviationweather-bldr.ncep.noaa.gov/sigmet/intl?hazard=mtw&loc=all'
my_html = requests.get(url)
my_html_text = my_html.text
soup = BeautifulSoup(my_html_text, 'html.parser')

sigmet_group = soup.find('pre')
sigmet_tags = sigmet_group.find_all('br')

for sigmet in sigmet_tags:
    sigmet_text = sigmet.previous
    coordinates_pattern = re.compile(r'[NS]\d{4}\s[WE]\d{5}', re.MULTILINE)
    matches = [match.group() for match in coordinates_pattern.finditer(sigmet_text)]
    match = re.search(r'\w{4}\s\w+\sFIR', sigmet_text)
    print(matches)
    print(match.group(), '\n')




