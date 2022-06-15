class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 0:
            return False
        
        hash = {}
        
        for n in nums:
            if n in hash:
                return True
            else:
                hash[n] = 1
        
        return False