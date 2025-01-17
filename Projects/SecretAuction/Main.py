import Auction_art

print(Auction_art.logo)
continueBidding = True

bids = {}


def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid price of {highest_bid}")


while continueBidding:
    name = input("What is your name: ")
    print(name)
    bidPrice = int(input("What is your Bid Price: $"))
    print(bidPrice)

    # Store the name and value in a dictionary
    bids[name] = bidPrice

    # Ask if there are any more bidders
    shouldWeContinue = input("Do you have any more bidders?: type yes or No. \n").lower()
    if shouldWeContinue == 'no':
        find_highest_bidder(bids)
        continueBidding = False
    elif shouldWeContinue == 'yes':
        print("\n"*20)
        continueBidding = True
