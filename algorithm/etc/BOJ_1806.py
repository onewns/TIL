import sys
sys.stdin = open('../input.txt', 'r')


n, m = map(int, input().split())
sums = [0] + list(map(int, input().split()))  # 시그마 배열 초기 세팅
for i in range(1, n+1):  # 시그마 배열 만들기
    sums[i] = sums[i] + sums[i-1]
if sums[-1] < m:
    print(0)
else:
    ans = float('inf')
    start_idx, end_idx = 0, 1
    while end_idx < n+1:
        temp = sums[end_idx] - sums[start_idx]
        if temp >= m:
            ans = min(ans, end_idx - start_idx)
            start_idx += 1
        else:
            end_idx += 1
    print(ans)
