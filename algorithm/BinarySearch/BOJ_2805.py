import sys
sys.stdin = open('../input.txt', 'r')

"""
def binary_search(height, start, end):
    left, right = start, end - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if height < trees[mid]:
            idx = mid
            left = mid + 1
        else:
            right = mid - 1
    return idx + 1


tree_num, need = map(int, input().split())
trees = sorted(list(map(int, input().split())), reverse=True)
accumulate_trees = [trees[0]]
for tree_idx in range(1, tree_num):
    accumulate_trees.append(accumulate_trees[tree_idx-1] + trees[tree_idx])
print(accumulate_trees)
ans = trees[0]
while need > 0:
    ans -= 1
    need -= binary_search(ans, 0, tree_num)
print(ans)
"""


def binary_search(start, end):
    left, right = start, end - 1  # 최소높이, 최대높이
    ans = 0  # 정확한 높이를 찾지 못햇을 때
    while left <= right:
        total = 0
        mid = (left + right) // 2
        for tree in trees:
            if tree - mid > 0:
                total += (tree - mid)
        if total == need:  # 정확한 값을 찾으면 더이상 진행 필요 x
            return mid
        elif total > need:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans


tree_num, need = map(int, input().split())
trees = list(map(int, input().split()))
print(binary_search(0, max(trees)))