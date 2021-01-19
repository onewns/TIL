import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
if n <= 99:
    print(n)
else:
    ans = 99
    for num in range(111, n + 1):
        num = str(num)
        diff = int(num[0]) - int(num[1])
        for i in range(1, len(num) - 1):
            if int(num[i]) - int(num[i + 1]) != diff:
                break
        else:
            ans += 1
    print(ans)
