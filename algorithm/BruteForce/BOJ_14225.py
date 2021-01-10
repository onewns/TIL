import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)
total = sum(nums)
possible = [0] * (total + 2)
possible[0] = 1
while nums:
    num = nums.pop()
    for i in range(total, -1, -1):
        if possible[i]:
            possible[i + num] = 1
for ans in range(1, total + 2):
    if not possible[ans]:
        print(ans)
        break
