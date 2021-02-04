import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
primes_sum = [0]
nums = [1] * (n+1)
for i in range(2, n + 1):
    if nums[i]:
        primes_sum.append(i)
        for k in range(i*2, n+1, i):
            nums[k] = 0
for i in range(1, len(primes_sum)):
    primes_sum[i] = primes_sum[i] + primes_sum[i-1]
ans = 0
# for j in range(len(primes_sum)-1, 0, -1):
#     for s in range(len(primes_sum) - j):
#         if primes_sum[s+j] - primes_sum[s] == n:
#             ans += 1
#             break
#         elif primes_sum[s+j] - primes_sum[s] > n:
#             breakgi
start_idx, end_idx = 0, 1
while end_idx < len(primes_sum):
    temp = primes_sum[end_idx] - primes_sum[start_idx]
    if temp == n:
        ans += 1
        start_idx += 1
    elif temp > n:
        start_idx += 1
    else:
        end_idx += 1
print(ans)
