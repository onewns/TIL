import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
dp = [[float('inf') for _ in range(n)] for _ in range(n)]
matrix = list(tuple(map(int, input().split())) for _ in range(n))
for start in range(n-1, -1, -1):
    dp[start][start] = 0
    for end in range(start + 1, n):
        num = float('inf')
        for i in range(start, end):
            temp = dp[start][i] + dp[i+1][end] + matrix[start][0] * matrix[i][1] * matrix[end][1]
            if temp < num:
                num = temp
        dp[start][end] = num
print(dp[0][n-1])


"""
딕셔너리가 검색이 더 오래 걸림...index를 정확히 특정할수 있다면 리스트를 쓰는게 낫다
한두번 min 연산은 괜찮지만 많을 경우 if를 사용하자
"""