class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
        
        for _ in range(zero_count):
            nums.remove(0)
        
        for _ in range(zero_count):
            nums.append(0)