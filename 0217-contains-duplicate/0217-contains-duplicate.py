class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_hash = {}
        
        for num in nums:
            if num in num_hash:
                return True
            
            num_hash[num] = 1
        
        return False
