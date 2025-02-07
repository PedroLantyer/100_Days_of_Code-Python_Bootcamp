from decimal import *


def get_total_bill_value():
    try:
        total_bill_value = float(input("What was the total bill? $").strip())
        if total_bill_value < 0:
            raise ValueError()
        return total_bill_value

    except ValueError:
        print("That doesn't seem like a valid bill, try again.", end="\n\n")
        return None

    
def get_tip_percentage():
    try:
        print("How much tip would you like to give?")
        tip_percent = int(input("10%, 12%, 15%? ").strip())
        
        match tip_percent:
            case 10 | 12 | 15:
                return tip_percent
            case _:
                raise ValueError

    except ValueError:
        print("That's not a valid tip, try again.", end="\n\n")
        return None


def get_people_count():
    try:
        count = int(input("How many people to split the bill? ").strip())
        if count < 1:
            raise ValueError
        return count
    
    except ValueError:
        print("That doesn't seem right to me, can you please repeat")
        return None


def get_tip_per_person(value: float, tip_percent: int, count: int):
    try:
        tip_value = ((Decimal(value) * (Decimal(1) + Decimal(tip_percent) / Decimal(100))) /
                     Decimal(count))
        return tip_value
    except Exception as err:
        print(err)
        return None


if __name__ == "__main__":
    print("Welcome to the tip calculator!", end="\n\n")
    
    while True:
        bill_value = get_total_bill_value()
        if bill_value is not None:
            break

    while True:
        tip_percentage = get_tip_percentage()
        if tip_percentage is not None:
            break

    while True:
        people_count = get_people_count()
        if people_count is not None:
            break

    tipPerPerson = get_tip_per_person(bill_value, tip_percentage, people_count)
    if tipPerPerson is not None:
        print(f"\nEach person should pay: ${tipPerPerson:.2f}")
        exit(0)
    exit(1)
