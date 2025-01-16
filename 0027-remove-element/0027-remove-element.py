class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for index, num in enumerate(nums):
            if num != val:
                nums[count] = nums[index]
                count += 1
        
        return count