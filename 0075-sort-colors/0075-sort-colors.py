class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3

        for num in nums:
            bucket[num] += 1
        
        j = 0
        for i in range(len(nums)):
            while bucket[j] <= 0:
                j += 1

            nums[i] = j
            bucket[j] -= 1

            
        
