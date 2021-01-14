import sys
sys.stdin = open('../input.txt', 'r')


string1 = ' ' + input()
string2 = ' ' + input()
dp = [list('' for _ in range(len(string1))) for _ in range(len(string2))]
for char2_idx in range(1, len(string2)):
    for char1_idx in range(1, len(string1)):
        if string2[char2_idx] == string1[char1_idx]:
            dp[char2_idx][char1_idx] = dp[char2_idx - 1][char1_idx - 1] + string1[char1_idx]
        else:
            if len(dp[char2_idx - 1][char1_idx]) > len(dp[char2_idx][char1_idx - 1]):
                dp[char2_idx][char1_idx] = dp[char2_idx - 1][char1_idx]
            else:
                dp[char2_idx][char1_idx] = dp[char2_idx][char1_idx - 1]
print(dp[-1][-1])