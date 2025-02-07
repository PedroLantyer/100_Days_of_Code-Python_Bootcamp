import re as regexp


class CaesarCypher:
    def __init__(self):
        self.mode: str = ""
        self.message: str = ""
        self.encodedMessage: str = ""
        self.shiftNumber: int = -1
        pass

    def set_mode(self):
        while True:
            user_input = input("type encode to encrypt, type decode to decrypt:\n").strip().lower()
            match user_input:
                case "encode":
                    self.mode = "encode"
                    break
                case "decode":
                    self.mode = "decode"
                    break
                case _:
                    print("Invalid option", end="\n\n")

    def set_message(self):
        while True:
            print()
            user_input = input("Type your message:\n")
            has_non_alpha = regexp.search("[^A-Za-z ]", user_input)
            if has_non_alpha is not None:
                print("Caesar Cyphers cannot contain non alpha values, please try again", end="\n\n")
            else:
                match self.mode:
                    case "encode":
                        self.message = user_input
                    case "decode":
                        self.encodedMessage = user_input
                    case _:
                        print("Invalid mode")
                        exit(1)
                break

    def set_shift_number(self):
        while True:
            print()
            user_input = input("Type the shift number:\n")
            is_positive_int = regexp.search("[^0-9]", user_input)
            if is_positive_int is not None or int(user_input) < 0:
                print("Shift number must be a positive or null integer")
            else:
                self.shiftNumber = int(user_input)
                if self.shiftNumber > 25:
                    self.shiftNumber %= 26
                break

    def encode_message(self):
        try:
            if self.shiftNumber < 0:
                raise Exception("Invalid shift number")

            for char in self.message:
                if char == " ":
                    self.encodedMessage += " "
                else:
                    ascii_value = ord(char)
                    ascii_value += self.shiftNumber
                    if char.isupper():
                        if ascii_value > 90:
                            ascii_value -= 26
                        self.encodedMessage += chr(ascii_value)
                    
                    elif char.islower():
                        if ascii_value > 122:
                            ascii_value -= 26
                        self.encodedMessage += chr(ascii_value)

            print()
            print(f"Encoded message:\n{self.encodedMessage}")
            return True
        
        except Exception as err:
            print(err)
            return False
        
    def decode_message(self):
        try:
            if self.shiftNumber < 0:
                raise Exception("Invalid shift number")
            
            for char in self.encodedMessage:
                if char == " ":
                    self.message += " "
                else:
                    ascii_value = ord(char)
                    ascii_value -= self.shiftNumber
                    
                    if char.isupper():
                        if ascii_value < 65:
                            ascii_value += 26
                        self.message += chr(ascii_value)
                    
                    elif char.islower():
                        if ascii_value < 97:
                            ascii_value += 26
                        self.message += chr(ascii_value)
            
            print()
            print(f"Decoded message:\n{self.message}")
            return True

        except Exception as err:
            print(err)
            return False
