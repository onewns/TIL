import sys
sys.stdin = open('../input.txt', 'r')


"""
시작 오후 4:21
끝 오후 4:45

1. 알파벳 별로 의미하는 자릿수 기록
2. 자릿수의 누적이 가장 큰 알파벳 부터 큰수를 할당
"""


def solution(n, words):
    answer = 0
    alpha_dic = {}
    for word in words:
        for i in range(len(word)):
            if word[i] in alpha_dic:
                alpha_dic[word[i]] += 10 ** (len(word) - i - 1)
            else:
                alpha_dic[word[i]] = 10 ** (len(word) - i - 1)
    alphas = sorted(alpha_dic.values(), key=lambda x: -x)
    for i in range(len(alphas)):
        answer += (9 - i) * alphas[i]

    return answer


N = int(input())
arr = [input() for _ in range(N)]
print(solution(N, arr))
