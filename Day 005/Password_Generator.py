import re as regexp
import random
from datetime import datetime

def genPwd(upperCaseLetterCount:int, lowerCaseLetterCount:int, symbolCount:int, numCount:int):
    try:
        countArr = [{"value" : upperCaseLetterCount, "type": "upper"}, 
                    {"value": lowerCaseLetterCount, "type": "lower"}, 
                    {"value": symbolCount, "type": "symbol"}, 
                    {"value": numCount, "type": "num"}]
        symbolArr = ("!", "#", "$", "%", "&")
        charCount = 0
        scrambleCount = 5
        for dict in countArr:
            charCount += dict["value"]
        
        pwd = []
        pwdScrambled = ""
        
        while len(pwd) < charCount:
            random.seed(datetime.now().timestamp() + (len(pwd) ** 2))
            if(len(countArr) == 1):
                index = 0
            elif(len(countArr) > 1):
                index = random.randint(0, len(countArr)-1)
            else:
                break
            type = countArr[index]["type"]

            if(countArr[index]["value"] == 0):
                countArr.pop(index)
                continue
            
            match type:
                case "upper":
                    pwd.append(chr(random.randint(65, 90)))
                case "lower":
                    pwd.append(chr(random.randint(97, 122)))
                case "symbol":
                    pwd.append(random.choice(symbolArr))
                case "num":
                    pwd.append(chr(random.randint(48, 57)))

            countArr[index]["value"] -= 1
        
        if(len(pwd) != charCount):
            raise Exception("Couldn't generate password with correct length") 

        for i in range(scrambleCount):
            while len(pwdScrambled) < charCount:
                random.seed(datetime.now().timestamp() + (len(pwdScrambled) ** 2))
                index = random.randint(0, len(pwd)-1)
                pwdScrambled += pwd[index]
                pwd.pop(index)
            if(i <= scrambleCount-1):
                pwd = list(pwdScrambled)

        return pwdScrambled
    
    except Exception as err:
        print(err)

def getUpperCaseLetterCount():
    while True:
        letterCount = input("How many upper case letters would you like in your password? ").strip()
        if(regexp.search("[^0-9]", letterCount) != None): #checks if there are any non numbers present
            print("Couldn't understand, please try again")
        else:
            return int(letterCount)
        
def getLowerCaseLetterCount():
    while True:
        letterCount = input("How many lower case letters would you like in your password? ").strip()
        if(regexp.search("[^0-9]", letterCount) != None): #checks if there are any non numbers present
            print("Couldn't understand, please try again")
        else:
            return int(letterCount)

def getSymbolCount():
    while True:
        symbolCount = input("How many symbols would you like in your password? ").strip()
        if(regexp.search("[^0-9]", symbolCount) != None):
            print("Couldn't understand, please try again")
        else:
            return int(symbolCount)

def getNumberCount():
    while True:
        numberCount = input("How many numbers would you like in your password? ").strip()
        if(regexp.search("[^0-9]", numberCount) != None):
            print("Couldn't understand, please try again")
        return int(numberCount)

if __name__ == "__main__":
    print("Random password generator", end="\n\n")
    
    upperCaseLetterCount = getUpperCaseLetterCount()
    lowerCaseLetterCount = getLowerCaseLetterCount()
    symbolCount = getSymbolCount()
    numCount = getNumberCount()
    
    pwd = genPwd(upperCaseLetterCount, lowerCaseLetterCount, symbolCount, numCount)
    if(pwd == None):
        exit(1)
    
    print(f"\nYour new password is:\n{pwd}")
    exit(0)

    