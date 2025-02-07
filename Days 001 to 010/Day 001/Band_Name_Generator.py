import os


def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")


def get_continue():
    while True:
        print("Do you wanna try again?")
        print("If Yes, type YES")
        print("If No, type NO")

        user_input = input()
        match user_input.upper():
            case "YES":
                clear_screen()
                return True
            case "NO":
                return False
            case _:
                print("Sorry I couldn't understand", end="\n\n")


if __name__ == "__main__":
    while True:
        print("Welcome to the Band Name Generator.", end="\n\n")

        city = input("What's the name of the city you grew up in?\n")
        pet_name = input("What's your pet's name?\n")

        clear_screen()
        print(f"Your band name could be {city} {pet_name}")

        if not get_continue():
            print("Goodbye", end="\n\n")
            exit(0)
