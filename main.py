import requests
from bs4 import BeautifulSoup

url = 'https://aviationweather-bldr.ncep.noaa.gov/sigmet/intl?hazard=mtw&loc=all'
my_html = requests.get(url)
my_html_text = my_html.text
soup = BeautifulSoup(my_html_text, 'html.parser')

sigmet_tags = soup.find_all('pre')

print(sigmet_tags[0].text)
