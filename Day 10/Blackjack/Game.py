from Card import Card
from os import getlogin
import secrets
from Contestant import Contestant

class Game:

    def __init__(self):
        self.turn:int = 1
        
        self.contestants: list[Contestant] = []
        cpu = Contestant(name="Computer", id=len(self.contestants))
        user = Contestant(name=getlogin(), id=len(self.contestants))
        self.contestants.append(cpu)
        self.contestants.append(user)

    def getHands(self):
        try:
            for contestant in self.contestants:
                print(f"{contestant.name} cards:", end=" ")
                for i in range(len(contestant.cards)):
                    card = contestant.cards[i]
                    if(i == len(contestant.cards)-1):
                        print(f"{card.name}")
                    else:
                        print(f"{card.name}",end=" ")
        except Exception as err:
            print(err)
            exit(1)
    
    def addCards(self, userAdds: bool):
        cpuAdds = secrets.choice((0, 1))
        if(cpuAdds):
            cpuCard = Card()
            self.contestants[0].cards.append(cpuCard)
        else:
            print("Computer passed", end="\n\n")
        
        if(userAdds):
            userCard = Card()
            self.contestants[1].cards.append(userCard)
        

    def setScores(self):
        try:
            for i in range(len(self.contestants)):
                tempScore:int = 0
                cont = self.contestants[i]
                for card in cont.cards:
                    if card.name != "Ace":
                        tempScore += card.value
                        if(tempScore > 21):
                            self.contestants[i].score = tempScore
                            continue
                    else:
                        if(tempScore <= 10):
                            tempScore += 11
                        else:
                            tempScore += 1
                
                self.contestants[i].score = tempScore
            self.turn += 1

        except Exception as err:
            print(err)
            exit(1)

    def checkOver(self):
        """Verifies if the game has ended"""
        for cont in self.contestants:
            if cont.score >= 21:
                return True
        return False

    def getWinner(self):
        try:
            contestantsRanked = sorted(self.contestants, key= lambda e: e.score, reverse=True)
            for cont in contestantsRanked:
                if cont.score > 21:
                    cont.score = 0
            
            print()
            if(contestantsRanked[0].score > contestantsRanked[1].score and contestantsRanked[0].score > 0):
                print(f"{contestantsRanked[0].name.upper()} WINS!")
                return
            elif(contestantsRanked[1].score > contestantsRanked[0].score and contestantsRanked[1].score > 0):
                print(f"{contestantsRanked[1].name.upper()} WINS!")
                return
            else:
                print(f"It's a draw.")
                return
            
        except Exception as err:
            print(err)
            exit(1)
            
                        
        