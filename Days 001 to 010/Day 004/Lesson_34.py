import random
from datetime import datetime

if __name__ == "__main__":
    friendsArr = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
    random.seed(datetime.now().timestamp())
    print(f"{random.choice(friendsArr)} pays the bill")
    
    exit(0)
