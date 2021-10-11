import sys
sys.stdin = open('../input.txt', 'r')
# from collections import deque
#
# subin, dong = map(int, input().split())
# subins = deque([subin])
# visited = [['no', 'no'] for _ in range(500001)]
# visited[subin][0] = 0
# time = 0
# while subins:
#     dong += time
#     if dong > 500000:
#         print(-1)
#         break
#     for _ in range(len(subins)):
#         subin = subins.popleft()
#         if visited[dong][time % 2] != 'no':
#             print(time)
#             sys.exit(0)
#         if 0 <= subin + 1 <= 500000 and visited[subin + 1][(time+1) % 2] == 'no':
#             visited[subin + 1][(time + 1) % 2] = time + 1
#             subins.append(subin + 1)
#         if 0 <= subin - 1 <= 500000 and visited[subin - 1][(time+1) % 2] == 'no':
#             visited[subin - 1][(time + 1) % 2] = time + 1
#             subins.append(subin - 1)
#         if 0 <= subin * 2 <= 500000 and visited[subin * 2][(time+1) % 2] == 'no':
#             visited[subin * 2][(time + 1) % 2] = time + 1
#             subins.append(subin * 2)
#     time += 1
# else:
#     print(-1)

subin, dong = map(int, input().split())
subins = [subin]
visited = [[-1, -1] for _ in range(500001)]
time = 0
visited[subin][0] = 0
while subins:
    dong += time
    if dong > 500000:
        print(-1)
        break
    if visited[dong][time % 2] != -1:
        print(time)
        break
    next_subins = []
    for subin in subins:
        for next_subin in [subin + 1, subin - 1, subin * 2]:
            if 0 <= next_subin <= 500000 and visited[next_subin][(time + 1) % 2] == -1:
                visited[next_subin][(time + 1) % 2] = time + 1
                next_subins.append(next_subin)
    subins = next_subins
    time += 1
else:
    print(-1)
