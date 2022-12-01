class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_hash = {}
        
        for index, num in enumerate(nums):
            numbers_hash[num] = index
            
        for index, num in enumerate(nums):
            if target - num in numbers_hash and index != numbers_hash[target - num]:
                return index, numbers_hash[target - num]
        
        return None
                