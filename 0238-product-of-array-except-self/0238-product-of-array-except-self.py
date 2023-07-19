class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left = 1
        right = 1
        
        for idx, num in enumerate(nums):
            output[idx] *= left
            left *= num
        
        for idx, num in enumerate(reversed(nums)):
            n = len(nums)-1
            output[n-idx] *= right
            right *= num
        
        return output
