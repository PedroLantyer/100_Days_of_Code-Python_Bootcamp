import secrets


class Card:
    def __init__(self):
        self.name = None
        self.value = None
        self.set_card()

    def set_card(self):
        card_id = secrets.choice(range(1, 13))

        match card_id:
            case 1:
                self.name = "Ace"
                self.value = 11
            case 11:
                self.name = "Jack"
                self.value = 10
            case 12:
                self.name = "Queen"
                self.value = 10
            case 13:
                self.name = "King"
                self.value = 10
            case num if 2 <= num <= 10:
                self.name = f"{num}"
                self.value = num
