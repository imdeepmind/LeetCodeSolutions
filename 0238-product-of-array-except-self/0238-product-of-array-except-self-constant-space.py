class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        left, right = 1, 1

        for num in nums:
            res.append(left)
            left *= num
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
