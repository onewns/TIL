import sys
sys.stdin = open("../input.txt", 'r')


from collections import deque


def truck_pass_time(trucks, weight):
    ready_q = deque(trucks)  # 남은 트럭들 큐
    bridge_q = deque()  # 다리위에 올라와 있는 큐
    truck_weight = ready_q.popleft()  # 첫번째 트럭의 무게
    weight -= truck_weight  # 제한하중 마이너스
    bridge_q.append((truck_weight, 1))  # 트럭무게와 함꼐 올라간 시간을 기록
    time = 2  # 1초 상황이 끝났으므로 2토 부터 시작
    while bridge_q:  # 다리위에 트럭이 없을때 까지
        if time - bridge_q[0][1] == bridge:  # 현재 시간과 다리의 선두에 있는 트럭의 진입시간 비교
            truck_weight, start_time = bridge_q.popleft()  # 다리를 벗어남
            weight += truck_weight  # 제한하중 플러스
        if ready_q and ready_q[0] <= weight:  # 현재 제한하중이 트럭보다 작거나 같다면
            truck_weight = ready_q.popleft()  # 다음트럭을
            bridge_q.append((truck_weight, time))  # 다리위에 올리고
            weight -= truck_weight  # 제한하중을 마이너스
        time += 1  # 다음시간을 탐색
    return time - 1


truck_num, bridge, limit = map(int, input().split())
print(truck_pass_time(list(map(int, input().split())), limit))

