class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        target = n * (n+1)//2

        current = 0
        for num in nums:
            current += num
        
        return target - current