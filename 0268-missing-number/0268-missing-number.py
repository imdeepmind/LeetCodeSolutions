class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        target = 0
        for i in range(n+1):
            target += i
        
        current = 0
        for num in nums:
            current += num
        
        return target - current