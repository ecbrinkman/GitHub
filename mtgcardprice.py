import json
import requests

API = "https://api.deckbrew.com/mtg/"

def cardinput():
   cardname = raw_input("Enter Card Name: ")
   print ("You wrote: " + cardname)
   cardname = cardname.replace(" ","-")
   cardname = cardname.replace(",","")
   cardname = cardname.lower()
   print ("You wrote: " + cardname)
   return cardname

def getcardjson(card):
   card = requests.get(API+"cards/"+card)
   if card.status_code == 200:   
      return card
   else:
      print "ERROR!"

   
cardname = cardinput()
r = getcardjson(cardname)
print r.status_code
price = r.json()["editions"][0]["price"]["median"]

print price
if price % 100 == 0 or price / 100 == 0:
   print "Median Price is: $%s0" % str(float(r.json()["editions"][0]["price"]["median"])/100)
else:
   print "Median Price is: $%s" % str(float(r.json()["editions"][0]["price"]["median"])/100) 
