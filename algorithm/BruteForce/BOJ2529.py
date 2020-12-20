import sys
sys.stdin = open("../input.txt", 'r')


def make_max(now, temp):
    global max_num
    if now == n:
        max_num = max(max_num, temp)
        return
    if now == -1:
        for i in range(9, 8-n, -1):
            max_visited[i] = True
            make_max(now + 1, temp + str(i))
            max_visited[i] = False
    else:
        for i in range(9, 8-n, -1):
            if not max_visited[i]:
                if operator[now] == '>' and temp[-1] > str(i):
                    max_visited[i] = True
                    make_max(now + 1, temp + str(i))
                    max_visited[i] = False
                elif operator[now] == '<' and temp[-1] < str(i):
                    max_visited[i] = True
                    make_max(now + 1, temp + str(i))
                    max_visited[i] = False


def make_min(now, temp):
    global min_num
    if now == n:
        min_num = min(min_num, temp)
        return
    if now == -1:
        for i in range(n+1):
            min_visited[i] = True
            make_min(now + 1, temp + str(i))
            min_visited[i] = False
    else:
        for i in range(n+1):
            if not min_visited[i]:
                if operator[now] == '>' and temp[-1] > str(i):
                    min_visited[i] = True
                    make_min(now + 1, temp + str(i))
                    min_visited[i] = False
                elif operator[now] == '<' and temp[-1] < str(i):
                    min_visited[i] = True
                    make_min(now + 1, temp + str(i))
                    min_visited[i] = False


n = int(input())
operator = list(input().split())
max_visited = {i: False for i in range(9, 8-n, -1)}
min_visited = {i: False for i in range(n + 1)}
min_num = '9876543210'
max_num = '0'
make_max(-1, '')
make_min(-1, '')
print(max_num)
print(min_num)