class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while end >= start:
            mid = end - (end - start) // 2
            midVal = nums[mid]

            if midVal == target:
                return mid
            
            if midVal > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1