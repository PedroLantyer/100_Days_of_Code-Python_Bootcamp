

def render_title():
    print("Hangman")

def render_current_guess(currentGuess: list[str]):
    print("".join(str(char) for char in currentGuess))