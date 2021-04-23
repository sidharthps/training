import requests
from parsel import Selector
url = 'http://google.com'
text = requests.get(url).text
selector = Selector(text=text)
Titile = selector.xpath('//title/text()')
print(Titile)