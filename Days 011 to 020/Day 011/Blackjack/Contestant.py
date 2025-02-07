from Card import Card


class Contestant:
    def __init__(self, name: str, contestant_id: int):
        self.cards: list[Card] = []
        self.score: int = 0
        print(name)
        try:
            if type(name) is not str:
                raise TypeError("Invalid value for name")
            if type(contestant_id) is not int:
                raise TypeError("Invalid value for id")
            self.name = name
            self.id = contestant_id

            for i in range(2):
                card = Card()
                self.cards.append(card)

        except TypeError as err:
            print(err)
            exit(1)
