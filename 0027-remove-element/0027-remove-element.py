class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        anchor, cur = 0, 0
        k = 0

        for num in nums:
            if num != val:
                k += 1
                nums[anchor], nums[cur] = nums[cur], nums[anchor]
                anchor += 1
            
            cur += 1
        
        return k