class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        index = right
        
        result = [0] * (right + 1)
        
        while index >= 0:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left]**2
                left += 1
            else:
                result[index] = nums[right]**2
                right -= 1
            
            index -= 1
        
        return result
        
        