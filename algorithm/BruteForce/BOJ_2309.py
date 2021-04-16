import sys
sys.stdin = open('../input.txt', 'r')


def solution(heights):
    heights.sort()
    over = sum(heights) - 100
    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            if heights[i] + heights[j] == over:
                del heights[j], heights[i]
                return heights


arr = [int(input()) for _ in range(9)]
print(*solution(arr), sep='\n')
