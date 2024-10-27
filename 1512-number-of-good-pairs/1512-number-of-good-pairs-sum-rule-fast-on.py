class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # ans = 0
        # for index1, num1 in enumerate(nums):
        #     for index2, num2 in enumerate(nums):
        #         if num1 == num2 and index1 < index2:
        #             ans += 1
        
        # return ans

        if len(nums) < 2:
            return 0

        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        ans = 0

        for k in hash:
            if hash[k] > 1:
                ans += (hash[k] * (hash[k] - 1)) // 2

        return ans
