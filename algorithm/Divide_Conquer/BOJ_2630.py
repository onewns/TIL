import sys
sys.stdin = open('../input.txt', 'r')


def check(start_y, start_x, l):
    global blue, white
    color = paper[start_y][start_x]
    for y in range(start_y, start_y + l):
        for x in range(start_x, start_x + l):
            if color != paper[y][x]:
                check(start_y, start_x, l // 2)
                check(start_y, start_x + l // 2, l // 2)
                check(start_y + l // 2, start_x, l // 2)
                check(start_y + l // 2, start_x + l // 2, l // 2)
                return
    if color:
        blue += 1
    else:
        white += 1


size = int(input())
paper = [list(map(int, input().split())) for _ in range(size)]
white = blue = 0
check(0, 0, size)
print(white)
print(blue)