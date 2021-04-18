import sys
sys.stdin = open('../input.txt', 'r')


limit, n = map(int, input().split())
nums = list(map(int, input().split()))
sums = {}
for n1_idx in range(n - 1):
    for n2_idx in range(n1_idx+1, n):
        s = nums[n1_idx] + nums[n2_idx]
        if s > limit - 2:
            continue
        if s in sums:
            sums[s].append([n1_idx, n2_idx])
        else:
            sums[s] = [[n1_idx, n2_idx]]
find = False
for s1, idx_lists in sums.items():
    for idx_list in idx_lists:
        if limit - s1 in sums:
            for idx_list1 in sums[limit - s1]:
                if idx_list1[0] not in idx_list and idx_list1[1] not in idx_list:
                    find = True
                    print('YES')
                    break
        if find:
            break
    if find:
        break
else:
    print('NO')