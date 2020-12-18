import sys
sys.stdin = open("../input.txt", 'r')


def dp():
    for now in range(2, repair_num + 2):  # 현재 위치 == now
        distance = 0  # 이미 지나온 정비소와의 거리
        for pre in range(now - 1, -1, -1):  # 이전 정비소를 탐색
            distance += between_distance[pre]  # 거리를 업데이트
            if distance > init_distance:  # 한번에 갈 수 있는 거리보다 이전 정보소의 거리가 커지면 정비해도 불가
                break
            if distance <= memo[pre][possible]:  # 전 정비소에서 정비 안하고 바로 now 정비소로 이동가능
                if memo[now][time] > memo[pre][time]:  # 현재 정비소의 시간보다 변화되는 값이 작다면
                    memo[now][time], memo[now][possible] = memo[pre][time], memo[pre][possible] - distance  # 업데이트
                    memo[now][repair_shop] = memo[pre][repair_shop]
            else:  # 전 정비소에서 정비를 해야함
                if memo[now][time] > memo[pre][time] + times[pre - 1]:
                    memo[now][time], memo[now][possible] = memo[pre][time] + times[pre - 1], init_distance - distance
                    memo[now][repair_shop] = memo[pre][repair_shop] + [pre]  # 슬라이싱 안해도 될거 같은데,,,
    print(memo[-1][time])
    print(len(memo[-1][repair_shop]))
    print(*memo[-1][repair_shop])


init_distance = int(input())
repair_num = int(input())
between_distance = list(map(int, input().split()))
times = list(map(int, input().split()))
INF, time, possible, repair_shop = float('inf'), 'time', 'possible', 'repair_shop'
memo = [{time: INF, possible: 0, repair_shop: []} for _ in range(repair_num + 2)]
memo[0][time], memo[0][possible] = 0, init_distance
memo[1][time], memo[1][possible] = 0, init_distance - between_distance[0]
dp()