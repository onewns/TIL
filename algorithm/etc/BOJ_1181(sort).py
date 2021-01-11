import sys
sys.stdin = open('../input.txt', 'r')


n = int(input())
words = list(set(input() for _ in range(n)))
words.sort(key=lambda x: (len(x), x))
print(*words, sep='\n')