class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_passes = [1] * len(nums)
        right_passes = [1] * len(nums)

        left = 1
        right = 1

        for index, num in enumerate(nums):
            left_passes[index] = left
            left *= num
        
        for i in range(len(nums)-1, -1, -1):
            right_passes[i] = right
            right *= nums[i]
        
        res = []

        for i in range(len(nums)):
            res.append(left_passes[i]*right_passes[i])
        
        return res