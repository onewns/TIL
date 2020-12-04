import sys
sys.stdin = open('12865.txt', 'r')


def comb(now, end, weight, value): # 조합사용 now = 물건 인덱스
    global ans
    if now == end: # 마지막 아이템에 다다르면
        ans = max(ans, value) # 둘중에 큰거로 ans 바꾸고
        return # 함수 종료
    if weight == limit_weight: # weight가 limit_weight 와 같으면
        ans = max(ans, value) # ans 를 큰거로 바꾸고
        return # 함수 종료
    if weight + items[now][0] <= limit_weight: # 가방에 더 들어간다면
        comb(now + 1, end, weight + items[now][0], value + items[now][1]) # 그 물건을 가방에 넣고 다음 물건 확인
    comb(now + 1, end, weight, value) # 그 물건을 가방에 넣지 않고 다음 물건 확인


ans = 0
item_num, limit_weight = map(int, input().split())
items = []
for _ in range(item_num):
    items.append(tuple(map(int, input().split())))
comb(0, item_num, 0, 0)
print(ans)
