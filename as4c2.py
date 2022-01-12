import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

for x in range(7):
    if x != 0:
        html = urllib.request.urlopen(tag, context=ctx).read()
    else:
        html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find_all('a')[17]['href']
print(tag)
