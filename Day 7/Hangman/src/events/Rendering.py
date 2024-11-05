#WIP

def renderTitle():
    print("Hangman")

def renderCurrentGuess(currentGuess: list[str]):
    print("".join(str(char) for char in currentGuess))