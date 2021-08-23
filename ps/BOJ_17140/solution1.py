import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def r_operator(arr):
    changed_arr = []
    max_length = len(arr[0])
    for row in arr:
        count_dic = {}
        for num in row:
            if num == 0:
                continue
            if num in count_dic:
                count_dic[num] += 1
            else:
                count_dic[num] = 1
        temp = sorted(count_dic.items(), key=lambda item: (item[1], item[0]))
        max_length = max(max_length, len(temp) * 2)
        changed_arr.append(temp)
    for i in range(len(changed_arr)):
        temp = changed_arr[i]
        new_row = []
        for elements in temp:
            new_row.extend(elements)
        new_row.extend([0] * (max_length - len(new_row)))
        changed_arr[i] = new_row
    return changed_arr


def c_operator(arr):
    changed_axis = change_axis(arr)
    changed_arr = r_operator(changed_axis)
    return_arr = change_axis(changed_arr)
    return return_arr


def change_axis(arr):
    changed_arr = [[] for _ in range(len(arr[0]))]
    for x in range(len(arr[0])):
        for y in range(len(arr)):
            changed_arr[x].append(arr[y][x])
    return changed_arr


def solution(r, c, k, arr):
    cnt = 0
    while cnt <= 100:
        if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
            return cnt
        if len(arr) >= len(arr[0]):
            arr = r_operator(arr)
        else:
            arr = c_operator(arr)
        cnt += 1
    return -1


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
print(solution(r, c, k, arr))
