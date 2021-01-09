import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
count = [0] * 10001
for _ in range(n):
    count[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)
