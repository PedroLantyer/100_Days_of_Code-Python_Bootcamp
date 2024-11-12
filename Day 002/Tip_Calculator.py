from decimal import *
import re as regex

def getTotalBillValue():
    try:
        totalBillValue = float(input("What was the total bill? $").strip())
        if(totalBillValue < 0):
            raise ValueError()
        return totalBillValue

    except ValueError:
        print("That doesn't seem like a valid bill, try again.", end="\n\n")
        return None

    
def getTipPercentage():
    try:
        print("How much tip would you like to give?")
        tipPercentage = int(input("10%, 12%, 15%? ").strip())
        
        match tipPercentage:
            case 10 | 12 | 15:
                return tipPercentage
            case _:
                raise ValueError

    except ValueError:
        print("That's not a valid tip, try again.", end="\n\n")
        return None

def getPeopleCount():
    try:
        peopleCount = int(input("How many people to split the bill? ").strip())
        if(peopleCount < 1):
            raise ValueError
        return  peopleCount
    
    except ValueError:
        print("That doesn't seem right to me, can you please repeat")
        return None

def getTipPerPerson(billValue: float, tipPercentage: int, peopleCount: int):
    try:
        tipValue = (Decimal(billValue) * (Decimal(1) + Decimal(tipPercentage) / Decimal(100))) / Decimal(peopleCount)
        return tipValue
    except Exception as err:
        print(err)
        return None


if __name__ == "__main__":
    print("Welcome to the tip calculator!", end="\n\n")
    
    while(True):
        billValue = getTotalBillValue()
        if(billValue != None):
            break

    while(True):
        tipPercentage = getTipPercentage()
        if(tipPercentage != None):
            break

    while(True):
        peopleCount = getPeopleCount()
        if(peopleCount != None):
            break

    tipPerPerson = getTipPerPerson(billValue, tipPercentage, peopleCount)
    if(tipPerPerson != None):
        print(f"\nEach person should pay: ${tipPerPerson:.2f}")
        exit(0)
    exit(1)

    

    
            