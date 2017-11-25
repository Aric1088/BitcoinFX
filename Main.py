import json
from urllib.request import urlopen
from lxml import html
import requests
import os
import time

#13f1989492032b11a1470f3b4d9fbbe7 <- api key for access
#apistring = http://apilayer.net/api/live?access_key=
#13f1989492032b11a1470f3b4d9fbbe7&currencies=USD,AUD,CAD,PLN,MXN&format=1


# Given a url of an api, takes the json representation and converts it
# into a dictionary
def decode_dict(url):
    return json.loads(urlopen(url).read().decode('utf-8'))

# Returns all the currencies from the bitcoin ticker
source ="https://blockchain.info/ticker"
bitcoin_dict = decode_dict(source)

# Scrapes foreign exchange data from google finance
def scrape_ccratio(basekey, conkey):
    page = requests.get("https://finance.google.com/finance/converter?a=1&from=" + basekey + "&to=" + conkey + "&")
    tree = html.fromstring(page.content)
    currencyratio = tree.xpath('//span[@class="bld"]/text()')
    return float(currencyratio[0].split()[0])

# Looks up specific value of item in bitdict
def lookup_bitval(key, bitdict):
    return (bitdict.get(key)).get("buy")

# Sees the buying and selling opportunities of two bitcoin markets
def convert_bitvalue(basekey, conkey, bdict):
    baseprice = lookup_bitval(basekey, bdict)
    conprice = lookup_bitval(conkey, bdict)
    baseconprice = conprice*(scrape_ccratio(conkey,basekey))
    conconprice = baseprice*(scrape_ccratio(basekey,conkey))
    s1 = "\nIt costs " + basekey + " " + str(baseprice) + " in " + basekey + " markets to obtain one bitcoin."
    s2 = " \nIt costs " + conkey + " " + str(conprice) + " in " + conkey +" markets to obtain one bitcoin."
    s3 = "\nBuying a bitcoin in " + conkey + " markets costs " + basekey + " " + str(baseconprice) + " equivalently."
    s4 = "\nBuying a bitcoin in " + basekey + " markets costs " + conkey + " " + str(conconprice) + " equivalently."
    analysis1 = "\nBuying a bitcoin in " + basekey + " markets and reselling in " + conkey + " markets would yield a net profit of " + basekey + " " + str(baseconprice - baseprice)
    analysis2 = "\nBuying a bitcoin in " + conkey + " markets and reselling in " + basekey + " markets would yield a net profit of " + conkey + " " + str(conconprice - conprice)
    return "\nBitcoin Price Analysis:\n\n" + s1 + s2 + s3 + s4 + analysis1 + analysis2



source ="https://blockchain.info/ticker"
bitcoin_dict = decode_dict(source)
while True:
    basekey = input("Enter a base currency: ")
    conkey = input("Enter your desired currency: ")
    while True:
        while True:
            try:

                print(tempstring)
                string = tempstring
            except:
                print("")
            stringl = (convert_bitvalue(basekey, conkey, bitcoin_dict))
            tempstring = stringl
            time.sleep(3)
            os.system('cls')
    try:
        while True:
            try:
                print(stringl)
            except:
                print("")
            stringl = (convert_bitvalue(basekey, conkey, bitcoin_dict))
            time.sleep(3)
            os.system('cls')
    except:
        print("Currency not found in database")
