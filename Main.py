import json
from urllib.request import urlopen
#13f1989492032b11a1470f3b4d9fbbe7 <- api key for access
#apistring = http://apilayer.net/api/live?access_key=
#13f1989492032b11a1470f3b4d9fbbe7&currencies=USD,AUD,CAD,PLN,MXN&format=1


# Given a url of an api, takes the json representation and converts it
# into a dictionary
def decode_dict(url):
    return json.loads(urlopen(url).read().decode('utf-8'))

# Returns all the currencies from the bitcoin ticker, and creates a string
# appending them all together for apilayer, returning a string of all them
# currencies in comparison to the US dollar
def currencies_to_string(dictx):
    currencies = dictx.keys()
    initstring = ""
    for i in currencies:
        initstring += i + ","
    initstring = initstring[:-1]
    initstring = "http://apilayer.net/api/live?access_key=13f1989492032b11a1470f3b4d9fbbe7&currencies=" + initstring + "&format=1"
    return initstring



def lookup_bitval(key, bitdict):
    tempdict = bitdict.get(key)
    buyval = tempdict.get("buy")
    sellval = tempdict.get("sell")
    return (key, buyval, sellval)



def convert_bitvalue(key2, bdict, cqdict):
    key = "USD" + key2
    usdata = lookup_bitval("USD", bdict)
    usprice = usdata[1]
    keydata = lookup_bitval(key2, bdict)
    keyprice =keydata[1]
    ccratio = cqdict.get(key)
    usconprice = keyprice/ccratio
    keyconprice = usprice/(1/ccratio)
    infos = "It costs USD " + str(usprice) + " in US markets to obtain one bitcoin. \nIt costs " + str(key2) + " " + str(keyprice) + " in " + key2 +" markets to obtain one bitcoin. \nBuying a bitcoin in " + str(key2) + " markets costs USD " + str(usconprice) + " equivalently. \nBuying a bitcoin in USD markets costs " + str(key2) + " " + str(keyconprice) + " equivalently."
    analysis1 = "\nBuying a bitcoin in USD markets and reselling in " + key2 + " markets would yield a net profit of USD " + str(usconprice - usprice)
    analysis2 = "\nBuying a bitcoin in " + key2 + " markets and reselling in USD markets would yield a net profit of " + key2 + " " + str(keyconprice - keyprice)
    return "\nBitcoin Price Analysis:\n\n" + infos + analysis1 + analysis2



source ="https://blockchain.info/ticker"
bitcoin_dict = decode_dict(source)
currency_dict = decode_dict(currencies_to_string(bitcoin_dict))
currency_quotes_dict = currency_dict.get("quotes")

while True:
    currentinput = input("Enter a currency: ")
    try:
        print(convert_bitvalue(currentinput, bitcoin_dict, currency_quotes_dict))
    except:
        print("Currency not found in database")
