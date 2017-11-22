import json
from urllib.request import urlopen
#13f1989492032b11a1470f3b4d9fbbe7 <- api key for access
#apistring = http://apilayer.net/api/live?access_key=
#13f1989492032b11a1470f3b4d9fbbe7&currencies=USD,AUD,CAD,PLN,MXN&format=1


bitdata = urlopen("https://blockchain.info/ticker")

bitdict = json.loads(bitdata.read().decode('utf-8'))
def ccratio(dictx):
    currencies = dictx.keys()
    initstring = ""
    for i in currencies:
        initstring += i + ","
    initstring = initstring[:-1]
    return initstring
apistring = "http://apilayer.net/api/live?access_key=13f1989492032b11a1470f3b4d9fbbe7&currencies=" + ccratio(bitdict) + "&format=1"
print(apistring)

ccdata = urlopen(apistring)
ccdict = json.loads(ccdata.read().decode('utf-8'))
print(ccdict)
    

def lookup(key):
    tempdict = bitdict.get(key)
    buyval = tempdict.get("buy")
    sellval = tempdict.get("sell")
    return (key, buyval, sellval)

print(lookup("USD"))

