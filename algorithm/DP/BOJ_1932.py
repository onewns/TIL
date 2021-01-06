import sys
sys.stdin = open('../input.txt', 'r')


row = int(input())
nums = [list(map(int, input().split())) for _ in range(row)]
for r in range(row-2, -1, -1):  # 밑에서 부터 보기
    for i in range(r+1):
        nums[r][i] += max(nums[r+1][i], nums[r+1][i+1])
print(nums[0][0])