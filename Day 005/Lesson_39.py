import sys

def getMaxValue(numArr: list[int]):
    try:
        if(len(numArr) == 0):
                raise Exception("Cant get Max Value -> Array is empty")
        
        #Gets minimal possible value for INT. Equivalent to -(2^63)
        maxValue = -sys.maxsize -1 
        
        if(len(numArr) == 0):
            return None

        for num in numArr:
            if(num > maxValue):
                maxValue = num
        return maxValue
    
    except Exception as err:
        print(err)

def getMinValue(numArr: list[int]):
    try:
        if(len(numArr) == 0):
            raise Exception("Cant get Max Value -> Array is empty")
        #Gets maximum possible value for INT. Equivalent to (2^63)-1
        minValue = sys.maxsize

        for num in numArr:
            if(num < minValue):
                minValue = num
        return minValue
    
    except Exception as err:
        print(err)



if __name__ == "__main__":
    studentScores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
    minValue, maxValue = getMaxValue(studentScores), getMinValue(studentScores)
    print(f"Max Value: {maxValue}") if maxValue != None else print("No Max Value")
    print(f"Min Value: {minValue}") if minValue != None else print("No Min Value")
    exit(0)