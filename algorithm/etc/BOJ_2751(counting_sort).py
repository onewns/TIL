import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


n = int(input())
count = {i: False for i in range(-1000000, 1000001)}
for _ in range(n):
    count[int(input())] = True
for i in count.keys():
    if count[i]:
        print(i)