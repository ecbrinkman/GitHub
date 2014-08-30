import json
import requests
import decimal

API = "https://api.deckbrew.com/mtg/"

def cardinput(): #takes no parameters, asks user for card name and returns it
   cardname = raw_input("Enter Card Name: ")
   print ("You wrote: " + cardname)
   cardname = cardname.replace(" ","-")
   cardname = cardname.replace(",","")
   cardname = cardname.lower()
   return cardname

def getcardjson(card): #takes a string and returns JSON object from the MtG API
   card = requests.get(API+"cards/"+card)
   if card.status_code == 200:   
      return card
   else:
      print "Card not found."
      exit()

def jsontoprice(json): #takes a JSON object and returns the price
   price = json.json()["editions"][0]["price"]["median"]
   price = decimal.Decimal(price) / 100
   return price

def printcardprice(price): #prints out the median cost of the card
   print "Median Price is: $%s" % price

   
cardname = cardinput()
r = getcardjson(cardname)
price = jsontoprice(r)
printcardprice(price)