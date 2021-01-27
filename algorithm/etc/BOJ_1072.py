import sys
import math
sys.stdin = open('../input.txt', 'r')


total, win = map(int, input().split())
rate = (win * 100) // total
if rate >= 99:
    print(-1)
else:
    print(math.ceil(((rate + 1) * total - (100 * win)) / (99 - rate)))
