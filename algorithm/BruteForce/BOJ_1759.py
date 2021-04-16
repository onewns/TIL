import sys
sys.stdin = open('../input.txt', 'r')
from itertools import combinations


def solution(l, c, alphabets):
    passwords = []
    alphabets.sort()
    vowel = ['a', 'e', 'i', 'o', 'u']
    for password in combinations(alphabets, l):
        vowel_cnt = 0
        cons_cnt = 0
        for char in password:
            if char in vowel:
                vowel_cnt += 1
                continue
            cons_cnt += 1
        if vowel_cnt > 0 and cons_cnt > 1:
            passwords.append(''.join(password))
    return passwords


L, C = map(int, input().split())
arr = input().split()
print(*solution(L, C, arr), sep='\n')
