import sys
sys.stdin = open('../input.txt', 'r')


def dfs(idy):
    global count
    if idy == n:
        count += 1
    else:
        for idx in range(n):
            if not x_visited[idx] and not right_down_visited[idx-idy] and not right_up_visited[idx+idy]:
                x_visited[idx] = 1
                right_down_visited[idx-idy] = 1 # 하향대각선
                right_up_visited[idx+idy] = 1
                dfs(idy + 1)
                x_visited[idx] = 0
                right_down_visited[idx-idy] = 0
                right_up_visited[idx+idy] = 0


n = int(input())
x_visited = [0] * n
right_up_visited = [0] * (2 * n - 1)
right_down_visited = [0] * (2 * n - 1)
count = 0
dfs(0)
print(count)
