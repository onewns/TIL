import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


n = int(input())
positives = []
negatives = []
for _ in range(n):
    num = int(input())
    if num > 0:
        positives.append(num)
    else:
        negatives.append(num)
positives.sort(reverse=True)
negatives.sort()
ans = 0
for p_idx in range(1, len(positives), 2):
    # 1 + 2 > 1 * 2 인 경우를 고려해줘야함
    ans += max(positives[p_idx] * positives[p_idx - 1], positives[p_idx] + positives[p_idx - 1])
for n_idx in range(1, len(negatives), 2):
    ans += negatives[n_idx] * negatives[n_idx - 1]
if len(positives) & 1:
    ans += positives[-1]
if len(negatives) & 1:
    ans += negatives[-1]
print(ans)