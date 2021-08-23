def get_primes(n):
    primes = [1] * (n + 1)
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = 0
    return primes


def solution(nums):
    nums.sort()
    primes = get_primes(nums[-1] + nums[-2] + nums[-3])
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if primes[nums[i] + nums[j] + nums[k]]:
                    answer += 1
    return answer
