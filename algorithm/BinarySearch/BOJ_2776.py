import sys
sys.stdin = open('../input.txt', 'r')


def binary_search(n, left, right):
    while left <= right:
        mid = (left + right) // 2
        if n < note1[mid]:
            right = mid - 1
        elif n > note1[mid]:
            left = mid + 1
        else:
            return 1
    return 0


for _ in range(int(input())):
    note1_num = int(input())
    note1 = sorted(list(map(int, input().split())))
    note2_num = int(input())
    note2 = list(map(int, input().split()))
    for num in note2:
        print(binary_search(num, 0, note1_num - 1))