import sys
sys.stdin = open('../input.txt', 'r')


def digit_sum(nums):
    s = 0
    for num in nums:
        s += int(num)
    return str(s)


n = input()
cnt = 0
while len(n) >= 2:
    n = digit_sum(n)
    cnt += 1
print(cnt)
if int(n) % 3:
    print('NO')
else:
    print('YES')