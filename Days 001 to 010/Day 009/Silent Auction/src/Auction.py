from operator import itemgetter

class Auction:
    def __init__(self):
        self.bidderArr:list = []
        self.highestBidder:dict[int, str, int | float] = {"id": 0, "name" : "", "bidValue": 0}
        pass

    def addBidder(self, bidder: dict[int, str, int | float]):
        if(type(bidder) != dict):
            print("Couldn't add bidder")
        else:
            self.bidderArr.append(bidder)

    def setHighestBidder(self):
        try:
            if len(self.bidderArr) >= 1:
                self.highestBidder = max(self.bidderArr, key=itemgetter("bidValue"))

        except Exception as err:
            print(err)
            print("Failed to set highest bidder")
            exit(1)

    def getAuctionWinner(self):
        try:
            if len(self.highestBidder["name"]) == 0:
                print("Can't get auction winner. No bids were placed")
            else:
                print(f"{"-" * 64: ^64}")
                print("Winner:")
                print(f"Id: {self.highestBidder["id"]}")
                print(f"Name: {self.highestBidder["name"]}")
                print(f"Bid: {self.highestBidder["bidValue"]:.2f}USD")
                print(f"{"-" * 64: ^64}")

        except Exception as err:
            print(err)
            print("Failed to get highest bidder")
            exit(1)