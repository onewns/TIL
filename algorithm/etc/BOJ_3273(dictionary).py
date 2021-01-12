import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
nums = dict(list(map(lambda x: (int(x), True), input().split())))
target = int(input())
ans = 0
for num in nums.keys():
    if (target - num) in nums:
        ans += 1
if ans & 1:
    print((ans - 1) // 2)
else:
    print(ans // 2)
