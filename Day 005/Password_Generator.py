import re as regexp
import random
from datetime import datetime


def gen_pwd(upper_case_letter_count: int, lower_case_letter_count: int, symbol_count: int, num_count: int):
    try:
        count_arr = [{"value": upper_case_letter_count, "type": "upper"},
                     {"value": lower_case_letter_count, "type": "lower"},
                     {"value": symbol_count, "type": "symbol"},
                     {"value": num_count, "type": "num"}]
        symbol_tuple = ("!", "#", "$", "%", "&")
        char_count = 0
        scramble_count = 5
        for dictionary in count_arr:
            char_count += dictionary["value"]

        new_password: list = []
        password_scrambled = ""

        while len(new_password) < char_count:
            random.seed(datetime.now().timestamp() + (len(new_password) ** 2))
            if len(count_arr) == 1:
                index = 0
            elif len(count_arr) > 1:
                index = random.randint(0, len(count_arr) - 1)
            else:
                break
            type_of_element = count_arr[index]["type"]

            if count_arr[index]["value"] == 0:
                count_arr.pop(index)
                continue

            match type_of_element:
                case "upper":
                    new_password.append(chr(random.randint(65, 90)))
                case "lower":
                    new_password.append(chr(random.randint(97, 122)))
                case "symbol":
                    new_password.append(random.choice(symbol_tuple))
                case "num":
                    new_password.append(chr(random.randint(48, 57)))

            count_arr[index]["value"] -= 1

        if len(new_password) != char_count:
            raise Exception("Couldn't generate password with correct length")

        for i in range(scramble_count):
            while len(password_scrambled) < char_count:
                random.seed(datetime.now().timestamp() + (len(password_scrambled) ** 2))
                index = random.randint(0, len(new_password) - 1)
                password_scrambled += new_password[index]
                new_password.pop(index)
            if i <= scramble_count - 1:
                new_password = list(password_scrambled)

        return password_scrambled

    except Exception as err:
        print(err)


def get_upper_case_letter_count():
    while True:
        letter_count = input("How many upper case letters would you like in your password? ").strip()
        if regexp.search("[^0-9]", letter_count) is not None:  # Checks if there are any non numbers present
            print("Couldn't understand, please try again")
        else:
            return int(letter_count)


def get_lower_case_letter_count():
    while True:
        letter_count = input("How many lower case letters would you like in your password? ").strip()
        if regexp.search("[^0-9]", letter_count) is not None:  # Checks if there are any non numbers present
            print("Couldn't understand, please try again")
        else:
            return int(letter_count)


def get_symbol_count():
    while True:
        symbol_count = input("How many symbols would you like in your password? ").strip()
        if regexp.search("[^0-9]", symbol_count) is not None:
            print("Couldn't understand, please try again")
        else:
            return int(symbol_count)


def get_number_count():
    while True:
        number_count = input("How many numbers would you like in your password? ").strip()
        if regexp.search("[^0-9]", number_count) is not None:
            print("Couldn't understand, please try again")
        return int(number_count)


if __name__ == "__main__":
    print("Random password generator", end="\n\n")

    upperCaseLetterCount = get_upper_case_letter_count()
    lowerCaseLetterCount = get_lower_case_letter_count()
    symbolCount = get_symbol_count()
    numCount = get_number_count()

    pwd = gen_pwd(upperCaseLetterCount, lowerCaseLetterCount, symbolCount, numCount)
    if pwd is None:
        exit(1)

    print(f"\nYour new password is:\n{pwd}")
    exit(0)
