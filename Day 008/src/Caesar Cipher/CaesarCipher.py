import re as regexp

class CaesarCipher:
    def __init__(self):
        self.mode: str = ""
        self.message:str = ""
        self.encodedMessage: str = ""
        self.shiftNumber: int = -1
        pass

    def setMode(self):
        while True:
            userInput = input("type encode to encrypt, type decode to decypt:\n").strip().lower()
            match userInput:
                case "encode":
                    self.mode = "encode"
                    break
                case "decode":
                    self.mode = "decode"
                    break
                case _:
                    print("Invalid option", end="\n\n")

    def setMessage(self):
        while True:
            print()
            userInput = input("Type your message:\n")
            hasNonAlpha = regexp.search("[^A-Za-z ]",userInput)
            if(hasNonAlpha != None):
                print("Ceaser Ciphers cannot contain non alpha values, please try again", end="\n\n")
            else:
                match(self.mode):
                    case "encode":
                        self.message = userInput
                    case "decode":
                        self.encodedMessage = userInput
                    case _:
                        print("Invalid mode")
                        exit(1)
                break

    def setShiftNumber(self):
        while True:
            print()
            userInput = input("Type the shift number:\n")
            isPositiveInt = regexp.search("[^0-9]", userInput)
            if(isPositiveInt != None or int(userInput) < 0):
                print("Shift number must be a positive or null integer")
            else:
                self.shiftNumber = int(userInput)
                if(self.shiftNumber > 25):
                    self.shiftNumber %= 26
                break

    def encodeMessage(self):
        try:
            if(self.shiftNumber < 0):
                raise Exception("Invalid shift number")

            for char in self.message:
                if(char == " "):
                    self.encodedMessage += " "
                else:
                    asciiValue = ord(char)
                    asciiValue += self.shiftNumber
                    if(char.isupper()):
                        if (asciiValue > 90):
                            asciiValue -= 26
                        self.encodedMessage += chr(asciiValue)
                    
                    elif(char.islower()):
                        if(asciiValue > 122):
                            asciiValue -= 26
                        self.encodedMessage += chr(asciiValue)

            print()
            print(f"Encoded message:\n{self.encodedMessage}")
            return True
        
        except Exception as err:
            print(err)
            return False
        
    def decodeMessage(self):
        try:
            if(self.shiftNumber < 0):
                raise Exception("Invalid shift number")
            
            for char in self.encodedMessage:
                if(char == " "):
                    self.message += " "
                else:
                    asciiValue = ord(char)
                    asciiValue -= self.shiftNumber
                    
                    if(char.isupper()):
                        if(asciiValue < 65):
                            asciiValue += 26
                        self.message += chr(asciiValue)
                    
                    elif(char.islower()):
                        if(asciiValue < 97):
                            asciiValue += 26
                        self.message += chr(asciiValue)
            
            print()
            print(f"Decoded message:\n{self.message}")
            return True

        except Exception as err:
            print(err)
            return False
