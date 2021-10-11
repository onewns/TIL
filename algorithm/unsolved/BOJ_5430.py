import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

for _ in range(int(input())):
    func = input()
    n = int(input())
    if n:
        nums = deque(input()[1:-1].split(','))
    else:
        nums = deque()
    for f in func:
        if f == 'R':
            nums.reverse()
        elif f == 'D':
            if len(nums):
                nums.popleft()
            else:
                print('error')
                break
    else:
        ans = ','.join(nums)
        print('['+ans+']')
