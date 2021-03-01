import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


n, m = map(int, input().split())
possibles = {}
q = deque([n])
possibles[n] = 1
if (m % 10) in [3, 5, 7, 9]:
    print(-1)
else:
    while q:
        k = q.popleft()
        double = k * 2
        right1 = k * 10 + 1
        if double == m or right1 == m:
            print(possibles[k] + 1)
            break
        if double < m:
            if double not in possibles:
                possibles[double] = possibles[k] + 1
                q.append(double)
        if right1 < m:
            if right1 not in possibles:
                possibles[right1] = possibles[k] + 1
                q.append(right1)
    else:
        print(-1)