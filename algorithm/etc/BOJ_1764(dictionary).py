import sys
sys.stdin = open('../input.txt', 'r')


n, m = map(int, input().split())
no_see = sorted(list(input() for _ in range(n)))
no_hear = {}
for _ in range(m):
    no_hear[input()] = True
ans = []
for person in no_see:
    if person in no_hear:
        ans.append(person)
print(len(ans))
print(*ans, sep='\n')