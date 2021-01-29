import sys
sys.stdin = open('../input.txt', 'r')


def is_palindrome(s, left, right):
    while left <= right:
        if s[left] != s[right]:
            return [False, left, right]
        left += 1
        right -= 1
    return [True, left, right]


for _ in range(int(input())):
    string = input()
    is_pal, left, right =  is_palindrome(string, 0, len(string) - 1)
    if is_pal:
        print(0)
    else:
        if is_palindrome(string, left+1, right)[0] or is_palindrome(string, left, right-1)[0]:
            print(1)
        else:
            print(2)
