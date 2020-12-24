import sys
sys.stdin = open("../input.txt", 'r')

"""
틀린이유 1
답이 없는 경우 -1을 출력하라함
새 물통이 필요 없는 경우 -1을 출력하라는 것으로 이해했으나
답이 없을수도 있다는 것을 배움
"""


def to_binary(n):  # 입력받은 수를 이진법으로 바꿈
    binary = []  # list로 처리
    while n >= 1:
        binary.append(n % 2)
        n //= 2
    return binary


def howmany(n, limit):
    bi = to_binary(n) + [0]  # 자릿수 올라가는 것을 고려
    cnt = 0
    while bi.count(1) > limit:  # 답이 나올때 까지 반복
        for i in range(len(bi)):  # 이진수를 검사
            if bi[i]:  # 0이 아니면 1이므로
                cnt += 2**i  # 필요한 물병을 더하고
                j = i + 1
                bi[j] += 1  # 자릿수를 올림
                bi[i] = 0
                while bi[j] == 2:  # 올린 자릿수가 2가 아닐때 까지 반복
                    bi[j] = 0
                    bi[j + 1] += 1
                    j += 1
                break
    return cnt


num, k = map(int, input().split())
print(howmany(num, k))
