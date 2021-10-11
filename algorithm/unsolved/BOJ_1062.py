import sys
sys.stdin = open('../input.txt', 'r')


"""
시작 오후 4:48
끝 오후 5:47
"""
from itertools import combinations


def word_to_bit(word):
    bit = 0b0
    word = set(word)
    for char in word:
        bit += (2 ** (ord(char)-97))

    return bit


def solution(n, k, words):
    if k < 5:
        return 0

    needs = set()
    for word in words:
        for char in word[4:-4]:
            needs.add(char)
    needs = needs.difference(('a', 'n', 't', 'i', 'c'))

    words = list(map(lambda x: x.replace('a', '').replace('n', '').replace('t', '').replace('i', '').replace('c', ''), words))
    words = list(map(word_to_bit, words))

    if len(needs) <= k - 5:
        return n

    cases = combinations(needs, k - 5)
    answer = 0
    for case in cases:
        a_bit = word_to_bit(''.join(case))
        temp = 0
        for word in words:
            if a_bit & word == word:
                temp += 1
        answer = max(answer, temp)
    return answer


N, K = map(int, input().split())
arr = [input() for _ in range(N)]
print(solution(N, K, arr))
