"""
2020_12_20 오후 8:54
pizzas를 큐에 넣고 꺼내면서 비교??
"""
import sys
sys.stdin = open('../input.txt', 'r')


def binary_search(n, start, end):
    left, right = start, end  # 이미 탐색에 맞춘 인덱스를 제공 (end - 1 x)
    idx = 0  # 피자가 들어갈 수 있는 깊이 인덱스
    while left <= right:
        mid = (left + right) // 2
        if n <= diameters[mid]:
            left = mid + 1
            idx = mid
        else:
            right = mid - 1
    return idx


depth, pizza_num = map(int, input().split())
diameters = [0] + list(map(int, input().split()))  # 높이를 쉽게 보기 위해 맨 앞에 [0] 추가
for i in range(2, depth + 1):  # 오븐의 깊이에 따른 직경 재 조정
    diameters[i] = min(diameters[i], diameters[i-1])
pizzas = list(map(int, input().split()))
for pizza in pizzas:
    depth = binary_search(pizza, 1, depth)  # 해당 피자가 들어갈 수 있는 깊이를 탐색
    if not depth:  # 0번 깊이라면 => 불가능 하다는 뜻
        print(depth)
        break
    depth -= 1  # 다음번 탐색을 위한 범위 조정
else:
    print(depth + 1)  # 탐색범위 조정으로 인한 깊이 복구
