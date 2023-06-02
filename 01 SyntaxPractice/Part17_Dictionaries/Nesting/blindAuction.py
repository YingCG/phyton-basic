
from click import clear


blindAuction ={}
    
print(blindAuction)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder_name in bidding_record:
        bid_amount = bidding_record[bidder_name]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder_name
    print(f"The winner is {winner} with bid of {highest_bid}")

bidding_finish = False
while not bidding_finish:
    name = input("what is your name? ")
    bid = float(input("What's your bid: $"))
    blindAuction[name] = bid
    anyMore = input("Anyone else like to bid? \n")
    if anyMore == 'no':
        bidding_finish = True
        find_highest_bidder(blindAuction)
    elif anyMore == "yes":
        clear()



