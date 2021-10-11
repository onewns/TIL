import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline
from collections import deque


n = int(input())
crops = deque([int(input()) for _ in range(n)])
ans = 0
time = 1
while crops:
    if crops[0] > crops[-1]:
        ans += crops.pop() * time
    elif crops[0] < crops[-1]:
        ans += crops.popleft() * time
    else:
        ans += crops.pop() * time
    time += 1
print(ans)