import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline
import heapq


hq = []
for _ in range(int(input())):
    heapq.heappush(hq, int(input()))
ans = 0
while len(hq) > 1:
    card1, card2 = heapq.heappop(hq), heapq.heappop(hq)
    ans += card1 + card2
    heapq.heappush(hq, card1 + card2)
print(ans)