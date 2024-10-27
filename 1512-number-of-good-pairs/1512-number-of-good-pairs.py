class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if num1 == num2 and index1 < index2:
                    ans += 1
        
        return ans