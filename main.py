from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
auction={}
def highest_bidder():
  max=0
  name1=""
  for key in auction:
    if(auction[key]>max):
      max=auction[key]
      name1=key
  print(f"{name1} is the highest bidder with a bid of ${auction[name1]}")

auction_person="yes"
while(auction_person=="yes"):
  name=input("What is your name? ")
  bid=int(input("What is your bid? $"))
  auction[name]=bid
  auction_person=input("Do you want another person to bid? Type 'yes' or 'no'. ")
  if(auction_person=="yes"):
    clear()
  else:
    highest_bidder()