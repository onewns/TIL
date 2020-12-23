import sys
sys.stdin = open("../input.txt", 'r')


def backtracking(now, cnt):
    global ans
    if cnt + (2 * size - 1 - now) <= ans:
        return
    if now == size*2 - 1:
        ans = max(cnt, ans)
        return
    y, x = min(size-1, now), max(0, now - size + 1)
    for _ in range(min(abs(y-x)+1, size)):
        if not visited[y-x] and arr[y][x]:
            visited[y-x] = True
            backtracking(now + 1, cnt + 1)
            visited[y-x] = False
        y -= 1
        x += 1
    backtracking(now + 1, cnt)


size = int(input())
arr = [list(map(int, input().split())) for _ in range(size)]
visited = {i: False for i in range(-size + 1, size)}
ans = 0
backtracking(0, 0)
print(ans)
