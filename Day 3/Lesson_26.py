import os

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Pizza:
    size: str
    hasPepperoni: bool
    hasExtraCheese: bool
    priceModifiers:list = [0,0,0]
    def __init__(self):
        pass

    def setSize(self):
        try:
            userInput = input("What size pizza do you want? S, M or L: ")
            match userInput.upper().strip():
                case "S":
                    self.size = "Small"
                    self.priceModifiers[0] = 15
                case "M":
                    self.size = "Medium"
                    self.priceModifiers[0] = 20
                case "L":
                    self.size = "Large"
                    self.priceModifiers[0] = 25
                case _:
                    raise ValueError("Couldn't define pizza size")
        except ValueError as error:
            print(error)
            return False

    def setHasPepperoni(self):
        try:
            userInput = input("Do you want pepperoni on your pizza? Y or N: ")
            match userInput.upper().strip():
                case "Y":
                    self.hasPepperoni = True
                case "N":
                    self.hasPepperoni = False
                case _:
                    raise ValueError("Couldn't define if the pizza has pepperoni")
        except ValueError as error:
            print(error)
            return False
        
    def setHasExtraCheese(self):
        try:
            userInput = input("Do you want extra cheese on your pizza? Y or N: ")
            match userInput.upper().strip():
                case "Y":
                    self.hasExtraCheese = True
                    self.priceModifiers[2] = 1
                case "N":
                    self.hasExtraCheese = False
                    self.priceModifiers[2] = 0
                case _:
                    raise ValueError("Couldn't define if the pizza has extra cheese")
        except ValueError as error:
            print(error)
            return False
        
    def setPrice(self):
        try:
            self.price:int = 0
            if(self.hasPepperoni):
                if(self.size == "Small"): 
                    self.priceModifiers[1] = 2
                else:
                    self.priceModifiers[1] = 3
            for priceMod in self.priceModifiers:
                self.price += priceMod
        except Exception as error:
            print(error)
            return False
    
    def printBill(self):
        try:
            clearScreen()
            print("*" * 30)
            print(f"1 {self.size} Pizza")
            print("Extra Cheese:", end=" ")
            print("Yes") if self.hasExtraCheese else print("No")
            print("Pepperoni:", end= " ")
            print("Yes") if self.hasPepperoni else print("No")
            print(f"Total Bill: ${self.price:.2f}")
            print("*" * 30)
        except Exception as error:
            print(error)
            return False


if __name__ == "__main__":
    print("Welcome to Python Pizza Deliveries!")
    pizzaObj = Pizza()
    if(pizzaObj.setSize() != None or pizzaObj.setHasPepperoni() != None or pizzaObj.setHasExtraCheese() != None):
        exit(1)
    if(pizzaObj.setPrice() != None or pizzaObj.printBill() != None):
        exit(1)
    
    exit(0)
    