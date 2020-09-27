#leetcode 238

class Solution:
    def productExceptSelf(self, nums):

        # my style timeout
        # answer = [(i,1) for i in range(len(nums))]
        # for i,n in enumerate(nums):
        #     answer = list(map(lambda x: [x[0],x[1]] if x[0] == i else [x[0],x[1]*n],answer))
        # answer = list(map(lambda x: x[1], answer))
        # return answer

        # use left, right 112ms 20.6MB
        answer = [1]
        for i in range(len(nums)-1):
            answer.append(answer[i]*nums[i])
        p = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i] * p
            p *= nums[i]
        return answer
a = Solution()
print(a.productExceptSelf([1,2,3,4]))