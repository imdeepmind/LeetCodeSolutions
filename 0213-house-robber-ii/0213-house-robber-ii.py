class Solution:
    def calc(self, nums):
        r1, r2 = 0, 0

        for num in nums:
            r1, r2 = r2, max(r1+num, r2)
        
        return r2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        return max(self.calc(nums[1:]), self.calc(nums[:-1]))