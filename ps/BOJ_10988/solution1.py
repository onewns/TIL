import sys
sys.stdin = open('PS/input.txt')
input = sys.stdin.readline

def solution(string):
  if is_palindrome(string):
    return 1
  return 0

def is_palindrome(string):
  if string == string[::-1]:
    return True
  return False


print(solution(input()))