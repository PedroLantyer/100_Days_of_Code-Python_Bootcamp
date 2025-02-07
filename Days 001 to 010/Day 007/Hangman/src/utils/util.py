import os


def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")


def get_matches(char: str, word: list[str] | str):
    match_ids = []
    for i in range(len(word)):
        if word[i] == char:
            match_ids.append(i)
    return match_ids
