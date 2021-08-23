import sys
sys.stdin = open('ps/input.txt')
input = sys.stdin.readline

def solution(N, Q, distances, questions):
    print(N)
    print(Q)
    print(distances)
    print(questions)
    return 

N, Q = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N-1)]
arr2 = [list(map(int, input().split())) for _ in range(Q)]
print(solution(N, Q, arr1, arr2))
