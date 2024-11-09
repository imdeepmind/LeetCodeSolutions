class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if num not in hash:
                hash[num] = 0
            else:
                return True
        
        return False
