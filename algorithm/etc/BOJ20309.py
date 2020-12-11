import sys
sys.stdin = open('../input.txt', 'r')


def is_possible_triple_sort(arr):  # 짝수번 인덱스에는 홀수, 홀수번 인덱스에는 짝수 가 와야 정렬 가능
    for i in range(len(arr)):  # 숫자 배열을 둘러보면서
        if not (arr[i] + i) & 1:  # 해당 숫자와 그 인덱스의 합이 홀수가 아니면
            return "NO"  # NO를 출력
    return "YES"  # 불가능한 부분이 없으면 YES 출력


n = int(input())
nums = list(map(int, input().split()))
print(is_possible_triple_sort(nums))