#import libraries
import bs4 as bs
import urllib3
from lxml import html
import requests
#Get webpage
#url = 'http://econpy.pythonanywhere.com/ex/001.html'
url = 'https://anzpremiership.co.nz/fixtures-and-results/seasons'
# http = urllib3.PoolManager()
# page = http.request('GET',url)
#tree = html.fromstring(page)
page = requests.get(url)
soup = bs.BeautifulSoup(page.text, 'lxml')
result = soup.find('h4', attrs={'class': 'listing-heading'})
print(soup.prettify())
print(result)