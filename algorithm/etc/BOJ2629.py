import sys
sys.stdin = open("../input.txt", 'r')


cn = int(input())
weights = list(map(int, input().split()))
wc = int(input())
check_list = list(map(int, input().split()))
possibles = {0}
ans = []
for weight in weights:
    for possible in list(possibles):
        possibles.add(possible + weight)
        possibles.add(abs(possible - weight))
for check in check_list:
    if check in possibles:
        ans.append("Y")
    else:
        ans.append("N")
print(*ans)