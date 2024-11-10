from Auction import Auction
from Bidder import Bidder
from Utils import *

if __name__ == "__main__":
    auction = Auction()

    while True:
        currentBidder = Bidder()
        
        bidderDict = currentBidder.getBidder(len(auction.bidderArr) + 1, auction.bidderArr)
        if (type(bidderDict) != dict):
            exit(1)
        
        auction.addBidder(bidderDict)
        done = not promptContinueGettingBidders()
        clearScreen()
        if(done):
            break

    auction.setHighestBidder()
    auction.getAuctionWinner()
    exit(0)