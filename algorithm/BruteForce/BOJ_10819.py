import sys
sys.stdin = open('../input.txt', 'r')
from itertools import permutations


def solution(n, nums):
    answer = 0
    cases = permutations(nums, n)
    for case in cases:
        temp = 0
        for i in range(n - 1):
            temp += abs(case[i] - case[i+1])
        answer = max(answer, temp)
    return answer


N = int(input())
arr = list(map(int, input().split()))
print(solution(N, arr))
