import sys
sys.stdin = open("../input.txt", 'r')


def bubble_sort(arr):  # 재귀로 구현
    arr = arr[:]
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            bubble_sort(arr)


# def bubble_sort(arr):  # 일반적인 버블소트
#     arr = arr[:]
#     for i in range(len(arr)-1):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 print(arr)


nums = list(map(int, input().split()))
bubble_sort(nums)