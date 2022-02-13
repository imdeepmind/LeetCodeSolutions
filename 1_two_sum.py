from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = {}
        
        for index, num in enumerate(nums):
            if not num in hash_num:
                hash_num[num] = index
            
            t = target - num
            if t in hash_num and hash_num[t] != index:
                return hash_num[t], index
