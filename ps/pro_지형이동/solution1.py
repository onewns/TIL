import heapq


def is_safe(y, x, size):
    if 0 <= y < size and 0 <= x < size:
        return True


def solution(land, height):
    answer = 0
    size = len(land)
    visited = [[0] * size for _ in range(size)]
    # (diff, y, x)
    visited[0][0] = 1
    q = []
    heapq.heappush(q, (abs(land[0][0] - land[1][0]), 0, 1))
    heapq.heappush(q, (abs(land[0][0] - land[0][1]), 1, 0))
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        cost, y, x = heapq.heappop(q)
        if not visited[y][x]:
            visited[y][x] = 1
            if cost > height:
                answer += cost
            for dy, dx in delta:
                ny, nx = y + dy, x + dx
                if is_safe(ny, nx, size) and not visited[ny][nx]:
                    heapq.heappush(q, (abs(land[y][x] - land[ny][nx]), ny, nx))

    return answer
