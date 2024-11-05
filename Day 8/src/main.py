from CaesarCipher import CaesarCipher
from Utils import *
from Rendering import renderTitle


if __name__ == "__main__":
    while True:
        renderTitle()
        cipherObj = CaesarCipher()
        cipherObj.setMode()
        cipherObj.setMessage()
        cipherObj.setShiftNumber()
        
        match cipherObj.mode:
            case "encode":
                success = cipherObj.encodeMessage()
                if(not success):
                    exit(1)
            case "decode":
                success = cipherObj.decodeMessage()
                if(not success):
                    exit(1)
            case _:
                print("Invalid Mode")
                exit(1)
        
        if(not getContinue()):
            exit(0)