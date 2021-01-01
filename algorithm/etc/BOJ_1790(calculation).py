import sys
sys.stdin = open('../input.txt', 'r')


n, k = map(int, input().split())
digit = 1  # 자릿수
for _ in range(1, 20):
    # 각 자리수 마다 최대 길이를 빼서 0 이상이면 빼줌
    if k - (9 * digit * (10 ** (digit - 1))) < 0:
        break
    k -= (9 * digit * (10 ** (digit - 1)))
    digit += 1  # 문제 없으면 자릿수 증가
#  줄어든 k와 현재 자릿수를 기반으로 어떤 숫자가 나오는지 구하고
num, remainder = (k // digit - 1) + (10 ** (digit - 1)), k % digit
if remainder:  # 나머지가 있으면
    num += 1  # 그 다음 숫자로 가서
    if num <= n:  # 가능한지 확인인
       print(str(num)[remainder - 1])
    else:
        print(-1)
else:  # 나머지가 없으면
    if num <= n:  # 가능한지 확인
        print(str(num)[-1])
    else:
        print(-1)
