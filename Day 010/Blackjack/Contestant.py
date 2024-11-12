from Card import Card

class Contestant:
    def __init__(self, name: str, id: int):
        self.cards: list[Card] = []
        self.score: int = 0
        try:
            if(type(name) != str):
                raise TypeError("Invalid value for name")
            if(type(id) != int):
                raise TypeError("Invalid value for id")
            self.name = name
            self.id = id
            
            for i in range(2):
                card = Card()
                self.cards.append(card)

        except TypeError as err:
            print(err)
            exit(1)