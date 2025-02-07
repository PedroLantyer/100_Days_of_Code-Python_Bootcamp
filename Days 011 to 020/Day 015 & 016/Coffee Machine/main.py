from CoffeeMachine import CoffeeMachine
from Util import *
from time import sleep

if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    while True:
        response: dict = coffee_machine.attempt_purchase()
        if response["mode"] == "terminate":
            clear_screen()
            print("GOODBYE")
            exit(0)
        if response["mode"] == "buy":
            sleep(5)
        clear_screen()
