import sys
sys.stdin = open('../input.txt', 'r')
from itertools import combinations


def solution(length, candidate, chars):
    chars.sort()
    passwords = []
    cases = combinations(chars, length)
    for case in cases:
        vowel = 0
        for char in case:
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
        if 0 < vowel <= length - 2:
            passwords.append(''.join(case))
    return '\n'.join(passwords)


L, C = map(int, input().split())
arr = input().split()
print(solution(L, C, arr))
