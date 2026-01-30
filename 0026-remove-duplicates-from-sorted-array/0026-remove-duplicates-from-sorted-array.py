class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        anchor = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[anchor] = nums[i]
                anchor += 1
        
        return anchor
        