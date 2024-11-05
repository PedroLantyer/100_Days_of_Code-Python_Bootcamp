import os

def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")

def getMatches(char: str, word: list[str] | str):
    matchIds = []
    for i in range(len(word)):
        if(word[i] == char):
            matchIds.append(i)
    return matchIds