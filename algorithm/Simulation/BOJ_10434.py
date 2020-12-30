import sys
sys.stdin = open('../input.txt', 'r')


def is_happy_num(num):
    if num in happy_nums:  # 이미 계산된 수라면
        return happy_nums[num]  # 결과 바로 표시
    visited = {num: 1}  # 아니라면 방문표시
    original_num = num
    while num != 1:  # 숫자가 1이 될 때 까지
        temp = 0
        for s in str(num):
            temp += int(s) ** 2
        if temp in happy_nums:  # temp가 happy_nums 안에 있으면
            is_happy = happy_nums[temp]  # 방문한 모든 숫자들(visited)은 결과를 공유
            for v in visited.keys():
                happy_nums[v] = is_happy
            break
        elif temp in visited:  # 방문했던 곳을 다시 방문하면 무한 반복
            for v in visited.keys():
                happy_nums[v] = False  # 행복한 수가 아님
            break
        elif temp == 1:  # 1이 되면
            for v in visited.keys():  # 현재 까지 방문한 경로는 행복한 수로 향하는 경로
                happy_nums[v] = True
        else:
            visited[temp] = 1
        num = temp
    return happy_nums[original_num]


is_prime_num = [1] * 10001  # 에라토스테네스의 체를 위한 준비 (인덱스가 각 수를 의미)
is_prime_num[0], is_prime_num[1] = 0, 0  # 1, 0은 소수 x
for i in range(10001):
    if is_prime_num[i]:  # 지워지지 않은 수면 소수
        for k in range(i * 2, 10001, i):
            is_prime_num[k] = 0  # 건너뛰며 지우기
happy_nums = {7: True, 313: True, 331: True, 367: True}  # 문제에서 제시된 행복한 수
for _ in range(int(input())):
    tc, n = map(int, input().split())
    if is_prime_num[n] and is_happy_num(n):
        print('{} {} YES'.format(tc, n))
    else:
        print('{} {} NO'.format(tc, n))
