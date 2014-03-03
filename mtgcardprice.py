import json
import urllib2

API = "https://api.deckbrew.com/mtg/"

cardname = raw_input("Enter Card Name: ")

print ("You wrote: " + cardname)
cardname = cardname.replace(" ","-")
cardname = cardname.replace(",","")
print ("You wrote: " + cardname)
response = urllib2.urlopen(API+"cards/"+cardname)
print response.geturl()

data = response.read()
#print data
parsed = json.loads(data)
#print json.dumps(parsed, indent=4, sort_keys=True)
print "Median Price is: $%s" % str(float(parsed["editions"][0]["price"]["median"])/100)