if __name__ == "__main__":
    for i in range(1, 101):
        if i % 3 != 0 and i % 5 != 0:
            print(i)
            continue
        elif i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        print()
    exit(0)
