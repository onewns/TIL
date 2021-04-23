import sys
sys.stdin = open('../input.txt', 'r')
"""
시뮬레이션
크게 어려운 점은 없는 문제
"""


def solution(limit, recommend):
    pictures = {}
    for i in range(len(recommend)):
        if recommend[i] in pictures:
            pictures[recommend[i]][0] += 1
            continue
        elif len(pictures) == limit:
            cnt = 1001
            order = 1001
            temp = 0
            for person, data in pictures.items():
                if data[0] < cnt or (data[0] == cnt and data[1] < order):
                    cnt, order, temp = data[0], data[1], person
            del pictures[temp]
        pictures[recommend[i]] = [1, i]
    answer = list(pictures.keys())
    answer.sort()
    return answer


N = int(input())
M = int(input())
arr = list(map(int, input().split()))
print(*solution(N, arr))
