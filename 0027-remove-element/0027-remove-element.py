class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            num = nums[i]

            if num != val:
                nums[count] = nums[i]
                count += 1
        
        return count