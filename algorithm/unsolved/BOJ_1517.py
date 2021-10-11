import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
arr = list(zip(range(n), map(int, input().split())))
print(arr)
arr.sort(key=lambda x: x[1])
print(arr)
ans = 0
for i in range(n):
    original_index, num = arr[i]
    ans += abs(i - original_index)
