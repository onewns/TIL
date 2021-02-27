import sys
sys.stdin = open('../input.txt', 'r')

# 팩토리얼에서 해당 숫자가 얼마나 있는지 구하는 함수
def counting_2_5(fac_num, prime):
    count = 0
    exponential = prime
    while fac_num >= exponential:
        count += fac_num // exponential
        exponential *= prime
    return count


n, m = map(int, input().split())
print(min(counting_2_5(n, 5) - counting_2_5(m, 5) - counting_2_5(n - m, 5), counting_2_5(n, 2) - counting_2_5(m, 2) - counting_2_5(n - m, 2)))
