class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_passes = []
        right_passes = []

        left = 1
        right = 1

        for num in nums:
            left_passes.append(left)
            left *= num
        
        for i in range(len(nums)-1, -1, -1):
            right_passes.append(right)
            right *= nums[i]

        right_passes = right_passes[::-1]

        res = []

        for i in range(len(left_passes)):
            res.append(left_passes[i] * right_passes[i])

        return res

        # [1,  2,  3, 4]
        # [1,  1,  2, 6] left
        # [24, 12, 4, 1] right

        # [24, 12, 8, 6] answer