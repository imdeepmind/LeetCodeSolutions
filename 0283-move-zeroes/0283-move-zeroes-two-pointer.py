class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero_count = 0

        # for num in nums:
        #     if num == 0:
        #         zero_count += 1
        
        # for _ in range(zero_count):
        #     nums.remove(0)
        #     nums.append(0)
        
        if len(nums) <= 1:
            return
        
        i, j = 0, 1

        while len(nums)-1 >= j:
            if nums[i] == 0:
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i, j = i+1, j+1
            else:
                i, j = i+1, j+1