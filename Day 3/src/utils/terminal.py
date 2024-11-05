import os

def clearScreen():
    if os.name.upper() == "NT":
        os.system("cls")
    else:
        os.system("clear")