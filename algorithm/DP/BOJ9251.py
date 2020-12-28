import sys
sys.stdin = open('../input.txt', 'r')


string1 = [0] + list(input())
string2 = [0] + list(input())
# dp 테이블
dp = [list(0 for _ in range(len(string1))) for _ in range(len(string2))]
for s2 in range(1, len(string2)):  # string2에서 s2번째 문자가 추가
    for s1 in range(1, len(string1)):  # string1에서 s1번째 문자가 추가 s2와 동시에 추가 되는상황
        if string2[s2] == string1[s1]:  # 추가되는 문자가 같다면
            # 전단계 (s1, s2 모두 추가되기 전 == [s2 - 1][s1 -1]) 에서 1을 증가
            dp[s2][s1] = dp[s2 - 1][s1 - 1] + 1
        else:  # 다르다면 두 문자가 추가되기전 상황에서 큰 수를 가져옴
            dp[s2][s1] = max(dp[s2 - 1][s1], dp[s2][s1 - 1])
print(dp[-1][-1])
