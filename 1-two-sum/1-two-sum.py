class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = {}
        
        for index, num in enumerate(nums):
            hash_num[num] = index
        
        for index, num in enumerate(nums):
            if target - num in hash_num and index != hash_num[target-num]:
                return [index, hash_num[target - num]]
        
        return []
