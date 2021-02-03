import sys
sys.stdin = open('../input.txt', 'r')


def back(depth, temp):
    global ans
    if temp > target:
        return
    ans = max(ans, temp)
    for n in nums:
        back(depth + 1, temp * 10 + n)


target, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
ans = 0
back(0, 0)
print(ans)