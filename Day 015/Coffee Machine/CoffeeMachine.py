import re as regex
import math
from decimal import Decimal, getcontext
from Util import clear_screen
from Resources import *
from time import sleep


class CoffeeMachine:

    def __init__(self):
        getcontext().prec = 9
        self.water_amount: int = 3000
        self.milk_amount: int = 2000
        self.coffee_amount: int = 1500
        self.coins: list[dict] = [{"id": 1, "count": 10, "value": Decimal("0.01"), "name": "Pennies"},
                                  {"id": 2, "count": 2, "value": Decimal("0.05"), "name": "Nickel"},
                                  {"id": 3, "count": 3, "value": Decimal("0.10"), "name": "Dimes"},
                                  {"id": 4, "count": 16, "value": Decimal("0.25"), "name": "Quarters"}, ]
        self.money: Decimal = Decimal("0")
        self.set_money()
        self.prices: list = []
        for element in coffee:
            self.prices.append(element["price"])

    def set_money(self):
        """
        Updates the amount of money currently in the machine
        """
        getcontext().prec = 9
        self.money = Decimal("0")
        for coin in self.coins:
            self.money += coin["value"] * coin["count"]

    def get_report(self):
        """
        Prints the coffee machine's report
        """
        clear_screen()
        print("*" * 45)
        print(f"Water: {self.water_amount}ml")
        print(f"Milk: {self.milk_amount}ml")
        print(f"Coffee: {self.coffee_amount}ml")
        print(f"Money: {self.money:.2f}USD")
        for coin in self.coins:
            print(f"{coin["name"]}: {coin["count"]}")
        print("*" * 45, end="\n\n")

        input("Press Enter to continue...")

    def increment_coin_count(self, coin_id: int, increment_value: Decimal):
        """
        Updates the count for each coin type in the machine
        """
        try:
            for coin in self.coins:
                if coin["id"] == coin_id:
                    coin["count"] += increment_value
                    if coin["count"] < 0:
                        raise ValueError("Decrement Count cannot be lower than coin count")

        except ValueError as err:
            print(err)
            return False
        except Exception as err:
            print(err)
            return False

    def get_menu(self):
        """
        Prints the menu
        """
        print("*" * 45)
        print("Menu:")
        print(f"1. Espresso   - {self.prices[0]: .2f}USD")
        print(f"2. Latte      - {self.prices[1]: .2f}USD")
        print(f"3. Cappuccino - {self.prices[2]: .2f}USD")
        print("*" * 45)

    def attempt_purchase(self) -> dict:
        """
        Attempts to purchase some coffee

        Returns:
            Dict: Dictionary with a boolean for success and a string for mode

        """
        try:
            getcontext().prec = 9
            self.get_menu()

            coffee_id: int = 0
            while True:
                coffee_chosen = input("What would you like? ").strip().lower()
                match coffee_chosen:
                    case "espresso" | "1":
                        coffee_id = 1
                        break
                    case "latte" | "2":
                        coffee_id = 2
                        break
                    case "cappuccino" | "3":
                        coffee_id = 3
                        break
                    case "report":
                        self.get_report()
                        return {"success": True, "mode": "report"}
                    case "terminate_pass_512":
                        return {"success": True, "mode": "terminate"}
                    case _:
                        print("Sorry, that's not a valid option", end="\n\n")
                        continue

            check_resources_response: dict = self.check_resources(coffee_id)
            if check_resources_response["success"] is False:
                return {"success": False, "mode": "buy"}
            resources_to_remove: dict = check_resources_response["resources_to_remove"]

            coffee_object = [element for element in coffee if coffee_id == element["id"]][0]

            money_inserted: Decimal = Decimal(0)
            coin_count: list[dict] = [{"id": 1, "name": "pennies", "count": 0, "value": Decimal("0.01")},
                                      {"id": 2, "name": "nickels", "count": 0, "value": Decimal("0.05")},
                                      {"id": 3, "name": "dimes", "count": 0, "value": Decimal("0.10")},
                                      {"id": 4, "name": "quarters", "count": 0, "value": Decimal("0.25")},]

            for i in range(len(coin_count), 0, -1):
                coin = coin_count[i - 1]
                while True:
                    current_coin = input(f"How many {coin["name"]}? ").strip()
                    if regex.search("[^0-9]", current_coin) is not None:
                        print("Sorry, that's not a valid option", end="\n\n")
                    else:
                        coin["count"] += int(current_coin)
                        money_inserted += coin["value"] * coin["count"]
                        break
            change_value: Decimal = money_inserted - coffee_object["price"]
            if change_value < 0:
                print("Sorry, that's not enough money. Money refunded")
                return {"success": False, "mode": "buy"}

            # Remove used coins
            check_money_response: dict = self.check_money(change_value)
            if check_money_response["success"] is False:
                print("Sorry, there's not enough change. Money refunded")
                return {"success": False, "mode": "buy"}

            # Remove used resources
            self.decrement_resources(resources_to_remove)
            coins_to_remove: list[dict] = check_money_response["coins_to_remove"]
            for coin in coins_to_remove:
                self.increment_coin_count(coin["id"], coin["count"])

            # Add coins
            for coin in coin_count:
                coin_id = coin["id"]
                self.increment_coin_count(coin_id, coin["count"])

            self.set_money()

            # If all verifications are successful
            if change_value > 0:
                print(f"Here's your tip: {change_value}")
                print("And", end="\n\n")

            clear_screen()
            for i in range(0, 4):
                sleep(1)
                if i < 3:
                    print(".", end="")
                else:
                    print()
            print(f"Here's your {coffee_object["flavour"]}. Enjoy")
            return {"success": True, "mode": "buy"}

        except Exception as err:
            print(err)
            return {"success": False, "mode": "buy"}

    def check_resources(self, coffee_id: int) -> dict:
        """
        Checks if there are enough resources for the selected coffee type

        Args:
            coffee_id  (int): id of the selected coffee type

        Returns:
            dict: Dictionary with a boolean and a dictionary for resources to be removed.
            If there are enough resources for the selected coffee type, the boolean is set to True
        """
        try:
            coffee_object = [element for element in coffee if element["id"] == coffee_id]

            if len(coffee_object) != 1:
                raise Exception("Coffee not found")
            if coffee_object[0]["water"] > self.water_amount:
                print("'Sorry there's not enough water")
                return {"success": False, "resources_to_remove": None}
            if coffee_object[0]["milk"] > self.milk_amount:
                print("Sorry there's not enough Milk")
                return {"success": False, "resources_to_remove": None}
            if coffee_object[0]["coffee"] > self.coffee_amount:
                print("Sorry there's not enough Coffee")
                return {"success": False, "resources_to_remove": None}

            resources_to_remove: dict = {"water": coffee_object[0]["water"],
                                         "milk": coffee_object[0]["milk"],
                                         "coffee": coffee_object[0]["coffee"]}

            return {"success": True, "resources_to_remove": resources_to_remove}
        except Exception as err:
            print(err)
            return {"success": False, "resources_to_remove": None}

    def check_money(self, change_value: Decimal) -> dict:
        """
        Checks if there is enough money for change

        Args:
            change_value (Decimal): Change value that needs to be paid to buyer

        Returns:
            An object with a boolean and the list of coins to be removed.
            If there is enough change, the boolean will be set to true
        """
        try:
            getcontext().prec = 6
            if change_value == 0:
                return {"success": True, "coins_to_remove": []}

            # Checks each coin type to see if there's enough money for change
            coins_lower: list[dict] = [coin for coin in self.coins if coin["value"] < change_value]
            coins_lower.sort(key=lambda coin: coin["value"], reverse=True)
            if len(coins_lower) == 0:
                return {"success": False, "coins_to_remove": []}

            remainder: Decimal = Decimal(change_value)
            coins_to_remove: list = []
            for coin in coins_lower:
                if coin["value"] <= remainder:
                    max_coins: Decimal = Decimal(math.floor(remainder / coin["value"]))
                    if max_coins == 0:
                        continue
                    if max_coins >= coin["count"]:
                        remainder -= coin["value"] * coin["count"]
                        coins_to_remove.append({"id": coin["id"], "count": -coin["count"]})
                    else:
                        remainder -= coin["value"] * max_coins
                        coins_to_remove.append({"id": coin["id"], "count": -max_coins})

            # After all coins have been tested, check if there's any remainder
            if remainder != 0:
                return {"success": False, "coins": []}

            return {"success": True, "coins_to_remove": coins_to_remove}
        except Exception as err:
            print(err)
            return {"success": False, "coins_to_remove": []}

    def decrement_resources(self, resources_to_remove: dict):
        """
        Removes resources after coffee has been produced

        Arguments:
            resources_to_remove {dict} -- Dictionary of resources to remove
        Returns:
            bool -- True if resources were removed, False otherwise
        """
        try:
            milk_removed = resources_to_remove["milk"]
            water_removed = resources_to_remove["water"]
            coffee_removed = resources_to_remove["coffee"]
            if self.milk_amount < self.milk_amount:
                raise ValueError("Cannot remove more milk than what is available")
            self.milk_amount -= milk_removed

            if self.water_amount < self.water_amount:
                raise ValueError("Cannot remove more water than what is available")
            self.water_amount -= water_removed

            if self.coffee_amount < self.coffee_amount:
                raise ValueError("Cannot remove more coffee than what is available")
            self.coffee_amount -= coffee_removed

            return True
        except ValueError as err:
            print(err)
            return False

        except Exception as err:
            print(err)
            return False
