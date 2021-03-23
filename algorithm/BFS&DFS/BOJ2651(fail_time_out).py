import sys
sys.stdin = open("../input.txt", 'r')


def dfs(now, distance, time, repair_shops):
    global ans
    if time >= ans[0]:  # 중간에 시간이 답보다 커지면 더할필요가 없음
        return
    if now == repair_num:  # 목적지에 도착하면
        ans[0] = min(ans[0], time)  # 작은값으로 업데이트
        ans[1] = repair_shops[:]  # 그때 상황의 정비소리스트 업데이트
        return
    repair_shops.append(now + 1)  # 수리하게 되면 정비소 추가
    dfs(now + 1, possible_distance - between_distance[now], time + times[now], repair_shops)  # 정비하는 경우
    repair_shops.pop()  # 정비리스트 초기화
    if distance >= between_distance[now]:
        dfs(now + 1, distance - between_distance[now], time, repair_shops)  # 정비하지 않는 경우


possible_distance = int(input())
repair_num = int(input())
between_distance = list(map(int, input().split()))
times = list(map(int, input().split()))
ans = [float('inf'), []]
memo = [float('inf') for _ in range(repair_num + 1)]
dfs(0, possible_distance - between_distance.pop(0), 0, [])
print('{}\n{}\n{}'.format(ans[0], len(ans[1]), ' '.join(list(map(str, ans[1])))))
