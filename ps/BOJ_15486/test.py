from solution2 import solution as correct
from solution3 import solution as compare
import random


day = 20


if __name__ == '__main__':
    for _ in range(100):
        day = 20
        arr = [(random.choice(range(1, 21)), random.choice(range(1, 1001)))
               for _ in range(day)]
        a, b = correct(day, arr), compare(day, arr)
        if not a == b:
            print(day, arr)
            break
    else:
        print('success')
