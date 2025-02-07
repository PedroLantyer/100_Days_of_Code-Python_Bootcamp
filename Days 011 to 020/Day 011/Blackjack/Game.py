from Card import Card
from os import getlogin
import secrets
from Contestant import Contestant


class Game:

    def __init__(self):
        self.turn: int = 1

        self.contestants: list[Contestant] = []
        cpu = Contestant(name="Computer", contestant_id=len(self.contestants))
        user = Contestant(name=getlogin(), contestant_id=len(self.contestants))
        self.contestants.append(cpu)
        self.contestants.append(user)

    def get_hands(self):
        try:
            for contestant in self.contestants:
                print(f"{contestant.name} cards:", end=" ")
                for i in range(len(contestant.cards)):
                    card = contestant.cards[i]
                    if i == len(contestant.cards) - 1:
                        print(f"{card.name}")
                    else:
                        print(f"{card.name}", end=" ")
        except Exception as err:
            print(err)
            exit(1)

    def add_cards(self, user_adds: bool):
        cpu_adds = secrets.choice((0, 1))
        if cpu_adds:
            cpu_card = Card()
            self.contestants[0].cards.append(cpu_card)
        else:
            print("Computer passed", end="\n\n")

        if user_adds:
            user_card = Card()
            self.contestants[1].cards.append(user_card)

    def set_scores(self):
        try:
            for i in range(len(self.contestants)):
                temp_score: int = 0
                cont = self.contestants[i]
                for card in cont.cards:
                    if card.name != "Ace":
                        temp_score += card.value
                        if temp_score > 21:
                            self.contestants[i].score = temp_score
                            continue
                    else:
                        if temp_score <= 10:
                            temp_score += 11
                        else:
                            temp_score += 1

                self.contestants[i].score = temp_score
            self.turn += 1

        except Exception as err:
            print(err)
            exit(1)

    def check_over(self):
        """Verifies if the game has ended"""
        for cont in self.contestants:
            if cont.score >= 21:
                return True
        return False

    def get_winner(self):
        try:
            contestants_ranked = sorted(self.contestants, key=lambda e: e.score, reverse=True)
            for cont in contestants_ranked:
                if cont.score > 21:
                    cont.score = 0

            print()
            if contestants_ranked[0].score > contestants_ranked[1].score and contestants_ranked[0].score > 0:
                print(f"{contestants_ranked[0].name.upper()} WINS!")
                return
            elif contestants_ranked[1].score > contestants_ranked[0].score and contestants_ranked[1].score > 0:
                print(f"{contestants_ranked[1].name.upper()} WINS!")
                return
            else:
                print(f"It's a draw.")
                return

        except Exception as err:
            print(err)
            exit(1)
