class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        
        first = 0
        last = len(nums) - 1
        middle = (first+last)/2
        middle = int(middle)
        
        while first <= last:
            if nums[middle]<target:
                first = middle+1
            elif nums[middle]==target:
                return middle
            else:
                last = middle-1
                
            middle = (first+last)/2
            middle = int(middle)
        
        return last+1