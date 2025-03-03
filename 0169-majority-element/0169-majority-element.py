from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapper = defaultdict(int)

        for num in nums:
            mapper[num] += 1
        
        max_value = 0
        max_item = None

        for key, value in mapper.items():
            if value > max_value:
                max_value = value
                max_item = key
        
        return max_item