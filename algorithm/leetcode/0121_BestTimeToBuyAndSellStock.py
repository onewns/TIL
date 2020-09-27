# leetcode 121
from typing import *

class Solution:
    def maxProfit(self, prices: List[int]):
        # my style timeout
        # ans = 0
        # for i in range(1,len(prices)):
        #     temp = max(prices[i:]) - min(prices[:i])
        #     if temp > ans:
        #         ans = temp
        # return ans

        # compare min with current 56ms 15MB
        min_price = 9876543210
        ans = 0
        for price in prices:
            min_price = min(price,min_price)
            ans = max(ans,price-min_price)
        return ans
a = Solution()
print(a.maxProfit([1,2,3,6,5,1]))