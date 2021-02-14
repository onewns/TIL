import sys
import heapq
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

hq = []
for _ in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(hq, (abs(n), n))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
