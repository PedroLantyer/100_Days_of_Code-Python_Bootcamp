from decimal import Decimal

coffee: list[dict] = [{"id": 1, "flavour": "Espresso", "water": 50, "coffee": 18, "milk": 0, "price": Decimal("1.50")},
                      {"id": 2, "flavour": "Latte", "water": 200, "coffee": 24, "milk": 150, "price": Decimal("2.50")},
                      {"id": 3, "flavour": "Cappuccino", "water": 250, "coffee": 24, "milk": 100,
                       "price": Decimal("3.00")}]

coins: list[dict] = [{"id": 1, "value": Decimal(0.01), "name": "Penny"},
                     {"id": 2, "value": Decimal(0.05), "name": "Nickel"},
                     {"id": 3, "value": Decimal(0.10), "name": "Dime"},
                     {"id": 4, "value": Decimal(0.25), "name": "Quarter"}]
