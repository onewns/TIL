import sys
from collections import deque


sys.stdin = open('../input.txt', 'r')


def simulation():
    cnt = 0
    zero = 0
    while zero < k:  # 내구도가 0인벨트가 조건보다 적은 동안
        belt.appendleft(belt.pop())  # 컨베이어벨트를 한칸씩 이동
        belt[n-1][0] = False  # 이동 시킨후 n 칸에 남아있으면 로봇 내리기
        for i in range(n-2, 0, -1):  # 선행 로봇부터 움직여야 하므로 뒤에서 부터 확인
            # 전칸에 로봇이 있고 다음칸이 비어 있으며 내구도가 남아있는 경우
            if belt[i][0] and not belt[i+1][0] and belt[i+1][1]:
                belt[i+1][0] = True  # 로봇을 옮기고
                belt[i][0] = False  # 로봇을 치우고
                belt[i+1][1] -= 1  # 내구도 1 감소
                if belt[i+1][1] == 0:  # 내구도가 변하된 벨트의 내구도가 0 이면
                    zero += 1  # 1 추가
        belt[n - 1][0] = False  # 로봇들이 이동한 후에 n 칸에 로봇이 있다면 내리기
        if belt[0][1]:  # 첫번째 칸에 내구도가 남아 있으며
            belt[0][0] = True  # 로봇을 올리고
            belt[0][1] -= 1  # 내구도 1 감소
            if belt[0][1] == 0:  # 내구도가 변화된 칸이 내구도가 0이 되면
                zero += 1  # 1 추가
        cnt += 1  # 단계 1 추가
    return cnt


n, k = map(int, input().split())
# 물건이 올라가 있는 상태와 내구도를 묶어서 표시
belt = deque(map(lambda x: [False, int(x)], input().split()))
print(simulation())
