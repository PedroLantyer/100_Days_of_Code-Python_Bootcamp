import sys


def get_max_value(num_arr: list[int]):
    try:
        if len(num_arr) == 0:
            raise Exception("Cant get Max Value -> Array is empty")

        # Gets minimal possible value for INT. Equivalent to -(2^63)
        max_value = -sys.maxsize - 1

        if len(num_arr) == 0:
            return None

        for num in num_arr:
            if num > max_value:
                max_value = num
        return max_value

    except Exception as err:
        print(err)


def get_min_value(num_arr: list[int]):
    try:
        if len(num_arr) == 0:
            raise Exception("Cant get Max Value -> Array is empty")
        # Gets maximum possible value for INT. Equivalent to (2^63)-1
        min_value = sys.maxsize

        for num in num_arr:
            if num < min_value:
                min_value = num
        return min_value

    except Exception as err:
        print(err)


if __name__ == "__main__":
    studentScores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
    minValue, maxValue = get_max_value(studentScores), get_min_value(studentScores)
    print(f"Max Value: {maxValue}") if maxValue is not None else print("No Max Value")
    print(f"Min Value: {minValue}") if minValue is not None else print("No Min Value")
    exit(0)
