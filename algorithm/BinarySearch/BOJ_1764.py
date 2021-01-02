import sys
sys.stdin = open('../input.txt', 'r')


def binary_search(name, start, end):
    left, right = start, end - 1
    while left <= right:
        mid = (left + right) // 2
        if name == no_hear[mid]:
            return True
        elif name < no_hear[mid]:
            right = mid - 1
        else:
            left = mid + 1


n, m = map(int, input().split())
no_see = sorted(list(input() for _ in range(n)))
no_hear = sorted(list(input() for _ in range(m)))
ans = []
for person in no_see:
    if binary_search(person, 0, m):
        ans.append(person)
print(len(ans))
print(*ans, sep='\n')
