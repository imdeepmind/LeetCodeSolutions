class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, num in enumerate(nums):
            delta = target - num
            if delta in hash:
                return [index, hash[delta]]
            
            hash[num] = index
        
        return [-1, -1]