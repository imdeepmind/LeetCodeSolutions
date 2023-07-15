class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for index, num in enumerate(nums):
            hash[num] = index
        
        for index, num in enumerate(nums):
            alpha = target - num
            
            if alpha in hash and hash[alpha] != index:
                return [index, hash[alpha]]
        
        return None
            