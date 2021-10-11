import sys
sys.stdin = open('../input.txt', 'r')


# def is_safe(r, c):
#     if 0 <= r < size and 0 <= c < size:
#         return True
#
#
# direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# size, trees_num, time = map(int, input().split())
# foods = [list(map(int, input().split())) for _ in range(size)]
# arr = list(list({'food': 5, 'trees': []} for _ in range(size)) for _ in range(size))
# for _ in range(trees_num):
#     row, col, age = map(int, input().split())
#     arr[row-1][col-1]['trees'].append(age)
# for _ in range(time):
#     # 봄
#     for row in range(size):
#         for col in range(size):
#             new_trees = []
#             for _ in range(len(arr[row][col]['trees'])):
#                 age = arr[row][col]['trees'].pop()
#                 if age <= arr[row][col]['food']:
#                     arr[row][col]['food'] -= age
#                     new_trees.append(age + 1)
#                 else:
#                     arr[row][col]['food'] += age // 2
#                     while arr[row][col]['trees']:
#                         arr[row][col]['food'] += arr[row][col]['trees'].pop() // 2
#                     break
#             arr[row][col]['trees'] = new_trees
#     # 가을
#     for row in range(size):
#         for col in range(size):
#             arr[row][col]['food'] += foods[row][col]
#             for tree in arr[row][col]['trees']:
#                 if not tree % 5:
#                     for dr, dc in direction:
#                         nr, nc = row + dr, col + dc
#                         if is_safe(nr, nc):
#                             arr[nr][nc]['trees'].append(1)
#             arr[row][col]['trees'].sort(reverse=True)
#
# ans = 0
# for row_index in range(size):
#     for col_index in range(size):
#         ans += len(arr[row_index][col_index]['trees'])
# print(ans)
