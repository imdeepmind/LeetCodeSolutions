class Solution:        
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        start, end = 0, len(nums) - 1
        
        while start <= end:
            k = end - ((end - start) // 2)

            if nums[k] == target:
                return k
            elif nums[k] < target:
                start = k + 1
            else:
                end = k - 1
        
        return -1