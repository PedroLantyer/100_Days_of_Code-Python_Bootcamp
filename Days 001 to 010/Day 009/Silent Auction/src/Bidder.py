import re as regex

class Bidder:
    def __init__(self):
        self.setName()
        self.setBid()

    def setName(self):
        while True:
            name = input("What is your name?: ")
            if(regex.search("[^A-Za-z ]", name) != None):
                print("Your name can only include letters and whitespaces", end="\n\n")
            elif (len(name.strip()) == 0):
                print("Your name cannot be empty", end="\n\n")
            else:
                self.name = name
                break

    def uniqueIdCheck(self, id: int, bidderArr: list[dict]):
        """Verifies if there are any duplicate Ids for Bidders"""
        try:
            for bidder in bidderArr:
                if(bidder["id"] == id):
                    return False
            return True
        except Exception as err:
            print(err)

    def setBid(self):
        try:
            while True:
                userInput = input("What's your bid?: $").strip()
                if(regex.search("[^0-9. ]", userInput) != None or len(regex.findall("[.]", userInput)) > 1 or len(userInput) == 0):
                    print("Your bid must be a valid number")
                elif(userInput == "0"):
                    print("Your bid must be higher than 0 USD")
                else:
                    self.bidValue = float(userInput)
                    break
        except Exception as err:
            print(err)
            print("Failed to set bid")
            exit(1)

    def getBidder(self, bidderId:int, bidderArr:list[dict]):
        if(len(self.name) == 0 or type(self.name) != str):
            print("Can't get bidder: No Name")
            return None
        if(type(self.bidValue) != int and type(self.bidValue) != float):
            print("Can't get bidder: No bid value")
            return None
        if(type(bidderId) != int):
            print("Can't get bidder: Invalid id")
            return None
        if(not self.uniqueIdCheck(bidderId, bidderArr)):
            print("Can't get bidder: Id is duplicate")
            return None

        bidderDict: dict[str, int | float] = {"id": bidderId, "name": self.name, "bidValue": self.bidValue}
        return bidderDict