import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(string):
    if is_palindrome(string):
        return 1
    return 0

def is_palindrome(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True


print(solution(input()))
