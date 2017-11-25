from lxml import html
import requests
page = requests.get('https://finance.google.com/finance/converter?a=1&from=USD&to=EUR&')
tree = html.fromstring(page.content)
currencyratio = tree.xpath('//span[@class="bld"]/text()')
print(currencyratio)
