class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapper = {}

        for num in nums:
            if num in mapper:
                return True
            
            mapper[num] = 1
        
        return False