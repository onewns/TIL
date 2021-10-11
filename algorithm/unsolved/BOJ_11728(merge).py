import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

new_arr = []
a_index, b_index = 0, 0
while a_index < n and b_index < m:
    if a[a_index] < b[b_index]:
        new_arr.append(a[a_index])
        a_index += 1
    else:
        new_arr.append(b[b_index])
        b_index += 1
new_arr += a[a_index:]
new_arr += b[b_index:]
print(*new_arr)