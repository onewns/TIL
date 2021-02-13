import sys
sys.stdin = open('../input.txt', 'r')


end1 = [[0, 0, 0], [0, 1, 0]]
end5 = [[0, 0, 0], [0, 0, 1]]
now = 1
n = int(input())
while n > now:
    now += 1
    end1.append([(end1[now-1][2] + end5[now-1][2]) % 1000000007,
                 (end1[now-1][0] + end5[now-1][0]) % 1000000007,
                 (end1[now-1][1] + end5[now-1][1]) % 1000000007])
    end5.append([(end1[now-1][1] + end5[now-1][1]) % 1000000007,
                 (end1[now-1][2] + end5[now-1][2]) % 1000000007,
                 (end1[now-1][0] + end5[now-1][0]) % 1000000007])
print(end5[n][0])