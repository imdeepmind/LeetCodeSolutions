class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left, right = 1, 1

        for i in range(len(nums)):
            val = nums[i]

            output[i] *= left
            left *= val
        
        for i in range(len(nums)-1, -1, -1):
            val = nums[i]

            output[i] *= right
            right *= val
        
        return output
