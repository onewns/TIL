import sys
sys.stdin = open('12865.txt', 'r')


def knapsack(): # 배낭문제
    pack = [] # 테이블
    for item_num in range(len(items) + 1): # 물건이 하나씩 추가되는 상황
        pack.append([]) # 추가되는 상황
        for weight in range(limit_weight + 1): # 용량이 1씩 늘어남
            if not item_num * weight: # 물건이 없거나 용량이 0 이면
                pack[item_num].append(0) # 당연히 값은 0
            elif items[item_num - 1][0] <= weight: # 새로 추가된 물건이 현재 가방 최대 용량보다 작거나 같으면
                pack[item_num].append(max( # 비교
                    # 새로 추가된 물건의 가치 + 물건이 새로 추가되며 남은 용량에 해당하는 최대값(물거니 없을때)
                    items[item_num-1][1] + pack[item_num-1][weight - items[item_num - 1][0]],
                    # 새로 추가된 물건을 안 넣은 상황(물건이 하나 없는 상태에서 해당 용량의 값)
                    pack[item_num - 1][weight]
                ))
            else: # 새로 추가된 물건이 현재 용량 보다 큰 경우 전 상황에서 최대값 가져오기
                pack[item_num].append(pack[item_num-1][weight])
    return pack[-1][-1] # 모든 물건, 최대 용량에서 최대 값


item_n, limit_weight = map(int, input().split())
items = []
for _ in range(item_n):
    items.append(tuple(map(int, input().split())))

print(knapsack())