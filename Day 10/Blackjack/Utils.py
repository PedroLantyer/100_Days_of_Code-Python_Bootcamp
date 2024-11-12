import os

def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")