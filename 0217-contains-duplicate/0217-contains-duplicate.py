class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _hash = {}

        for num in nums:
            if num in _hash:
                return True
            
            _hash[num] = 1
        
        return False