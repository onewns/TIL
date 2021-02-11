import sys
sys.stdin = open('../input.txt', 'r')

"""
오름차순 정렬후 누적합을 구해 나간다.
다음 번 무게가 현재 누적합 + 1이 아니라면 뒤로 갈수록 무거워 지므로 누적합 + 1을 구할 수 있는 방법이 없다
"""

n = int(input())
weights = list(map(int, input().split()))
weights.sort()
temp = 0
for weight in weights:
    if weight > temp + 1:
        print(temp + 1)
        break
    temp += weight
else:
    print(temp + 1)