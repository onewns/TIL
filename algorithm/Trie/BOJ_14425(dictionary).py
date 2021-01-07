import sys
sys.stdin = open('../input.txt', 'r')


n, m = map(int, input().split())
trie = {}  # 트라이
for _ in range(n):
    cur = trie  # 일종의 head
    for char in input():  # 문자열 각각의 문자를 순서대로 검사
        if char in cur:  # 이미 만들어진 노드가 있으면
            cur = cur[char]  # 그대로 통과
        else:  # 없으면
            cur[char] = {}  # 노드를 새로 만들고
            cur = cur[char]  # 만든 노드로 이동
    cur['#'] = '#'  # 문자열이 끝남을 표시
ans = 0
for _ in range(m):
    cur = trie
    for char in input():
        if char in cur:
            cur = cur[char]
        else:
            break
    else:
        if '#' in cur:
            ans += 1
print(ans)
