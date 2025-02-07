from CaesarCipher import CaesarCypher
from Utils import *
from Rendering import render_title


if __name__ == "__main__":
    while True:
        render_title()
        cipherObj = CaesarCypher()
        cipherObj.set_mode()
        cipherObj.set_message()
        cipherObj.set_shift_number()
        
        match cipherObj.mode:
            case "encode":
                success = cipherObj.encode_message()
                if not success:
                    exit(1)
            case "decode":
                success = cipherObj.decode_message()
                if not success:
                    exit(1)
            case _:
                print("Invalid Mode")
                exit(1)
        
        if not get_continue():
            exit(0)
